from django.urls import path
from .views import upload_cart,cart_list


urlpatterns=[path("Cart/upload",upload_cart,name="shoppingcart_upload_view"),
             path("Cart/list",cart_list,name="cart_list_view"),
             
             
            ]