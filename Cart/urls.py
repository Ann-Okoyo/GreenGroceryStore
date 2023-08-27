from django.urls import path
from .views import upload_cart,cart_list
from .views import cart_detail
from .views import edit_cart_view


urlpatterns=[path("Cart/upload",upload_cart,name="shoppingcart_upload_view"),
             path("Cart/list",cart_list,name="cart_list_view"),
             path("Cart/<int:id>/",cart_detail,name="cart_details_view"),
             path("Cart/edit/<int:id>/",edit_cart_view,name="edit_cart_view"),
             
             
            ]