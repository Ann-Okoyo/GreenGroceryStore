
from django.urls import path
from .views import AddToCartView, CartListView, CustomerDetailView, CustomerListView, OrderDetailView, OrderListView, ProductDetailView, ProductListView


urlpatterns = [
    path("customer/", CustomerListView.as_view(), name="customer_list_view"),
    # path("customer/<int:id>/",CustomerListView.as_view(),name="customer_detail")
    path("products/", ProductListView.as_view(), name="product_list_view"),
    path ("products/<int:id>/",  ProductDetailView.as_view(), name ="product_detail_view"),
    path("orders/", OrderListView.as_view(), name="order_list_view"),
    path ("orders/<int:id>/",  OrderDetailView.as_view(), name ="order_detail_view"),
    path("cart/", CartListView.as_view(), name="cart_list_view"),
    path("add_to_cart/", AddToCartView.as_view(), name= "Add_to_cart"),
]

