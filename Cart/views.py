from django.shortcuts import render
from .forms import CartuploadForm
from .models import Basket

# Create your views here.
def upload_cart(request):
    if request.method == "POST":
        form = CartuploadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CartuploadForm()

    return render(request, "cart/shoppingcart_upload.html", {"form": form})
def cart_list(request):
    basket = Basket.objects.all()
    return render(request, "cart/cart_list.html", {"basket": basket})

def cart_detail(request,id):
    cart=Basket.objects.get(id=id)
    return render(request,"cart/cart_detail.html",{"cart":cart})


def edit_cart_view(request,id):
    cart=Basket.objects.get(id=id)
    if request.method == 'POST':
        form=CartuploadForm(request.POST,instance=cart)
        if form.is_valid():
            form.save()
        return redirect("cart_detail_view,id=id")
    else:
        form=CartuploadForm(request.POST,instance=cart)
        return render(request,"cart/edit_cart.html",{"form":form})




# def product_details(request, id):
#     product = Product.objects.get(id=id)
#     return render(request,"inventory/product_details.html",{"product": product})
