from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import *
from datetime import datetime



# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def add_product(request):
    if request.method == 'POST':
        data = request.POST

        Product_name = data.get('product')
        Product_price = data.get('price')

        if not Products.objects.filter(Product_name=Product_name).exists():
            Products.objects.create(
                Product_name = Product_name,
                Product_price = Product_price,
                )            
            return redirect('add_product')
        
        else:
            message = "Product Already Exist!"

    qureyset = Products.objects.all()

    context = {'Product' : qureyset,'message' : message if request.method == 'POST' else '',}

    return render(request, 'Product/Add_product.html' , context)

def product_list(request):

    qureyset = Products.objects.all()

    context = {'Product' : qureyset}

    return render(request, 'Product/product_list.html',context)

def delete_Product(request,id):

    qset = Products.objects.get(id=id)
    qset.delete() 
    return redirect('product_list')

def update_Product(request,id):

    qureyset = Products.objects.get(id = id)

    if request.method == 'POST':
        data = request.POST

        Product_name = data.get('product')
        Product_price = data.get('price')
        
        qureyset.Product_name = Product_name
        qureyset.Product_price = Product_price

        qureyset.save()

        return redirect('product_list')



    context = {'Products' : qureyset}

    return render( request,'Product/update_Product.html',context )


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def create_Bill(request):
    if request.method == 'POST':
        if 'save_pdf' in request.POST:
            qset = Product_Bill.objects.all()
            total = sum(item.Price * item.Quantity for item in qset)
            return generate_pdf(qset, total)

        data = request.POST
        Name = data.get('Product')
        Price = int(data.get('Price'))
        Quantity = int(data.get('Quantity'))
        Total_Price = Price * Quantity

        Product_Bill.objects.create(
            Name=Name,
            Price=Price,
            Quantity=Quantity,
            Total_price=Total_Price,
        )
        
        return redirect('create_bill')

    qset = Product_Bill.objects.all()
    total = sum(item.Price * item.Quantity for item in qset)

    context = {'Product_Bill': qset, 'total': total}
    return render(request, "Bills/create_bill.html", context)

def generate_pdf(Product_Bill, total):
    template_path = 'Bills/pdf_template.html'

    current_date = datetime.now()
    formatted_date = current_date.strftime('%d-%m-%y')

    context = {
        'Product_Bill': Product_Bill,
        'total': total,
        'current_date' : formatted_date
    }

    # Render HTML to string
    template = get_template(template_path)
    html = template.render(context)

    # Generate the PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="bill.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def delete_bill(request):

    Product_Bill.objects.all().delete()

    return redirect('create_bill')