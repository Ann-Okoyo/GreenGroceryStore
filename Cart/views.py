from django.shortcuts import render
from .forms import CartuploadForm
from .models import Basket

# Create your views here.
def upload_cart(request):
    if request.method == "POST":
        form = CartuploadForm(request.POST, request.Files)
        if form.is_valid():
            form.save()
    else:
        form = CartuploadForm()

    return render(request, "cart/shoppingcart_upload.html", {"form": form})
def cart_list(request):
    basket = Basket.objects.all()
    return render(request, "cart/cart_list.html", {"basket": basket})
# def product_details(request, id):
#     product = Product.objects.get(id=id)
#     return render(request,"inventory/product_details.html",{"product": product})
