from django.shortcuts import render
from .forms import ProductuploadForm
from inventory.models import Product
from django.shortcuts import redirect

def upload_product(request):
    if request.method == "POST":
        form = ProductuploadForm(request.POST, request.Files)
        if form.is_valid():
            form.save()
    else:
        form = ProductuploadForm()

    return render(request, "inventory/product_upload.html", {"form": form})

def products_list(request):
    products = Product.objects.all()
    return render(request, "inventory/products_list.html", {"products": products})

def product_details(request, id):
    product = Product.objects.get(id=id)
    return render(request,"inventory/product_details.html",{"product": product})

from django.shortcuts import redirect, render
from .models import Product
from .forms import ProductuploadForm

def edit_product_view(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductuploadForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_detail_view", id=id)
        else:
            form = ProductuploadForm(request.POST, instance=product)
            return render(request, "inventory/edit_product.html", {"form": form})
    else:
        form = ProductuploadForm(instance=product)
        return render(request, "inventory/edit_product.html", {"form": form})