from django.urls import path
from .views import upload_product
from .views import products_list
from .views import product_details
from .views import edit_product_view

urlpatterns=[path("products/upload",upload_product,name="upload_product"),
             path("products/list",products_list,name="products_list"),
             path("products/<int:id>/",product_details,name = "product_details"),
             path("product/edit/<int:id>/",edit_product_view,name="edit_product_view"),
             
             ]