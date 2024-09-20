from .views import *
from django.urls import path

urlpatterns = [
    path('',home_view,name='home'),
    path('add_product/',add_product,name='add_product'),
    path('product_list/',product_list,name='product_list'),
    path('delete_product/<int:id>/',delete_Product,name='delete_product'),
    path('update_product/<int:id>/',update_Product,name='update_product'),
    # --------------------------------------------------------------------------
    path('create_bill/',create_Bill,name='create_bill'),
    path('bill',generate_pdf,name='bill'),
    path('delete_bill',delete_bill,name='delete_bill'),
    # --------------------------------------------------------------------------
    
]