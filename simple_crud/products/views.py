from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
# Create your views here.


def list_products(request):
    prod = Product.objects.all()
    return render(request, 'products.html', context={'products': prod})


def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list')

    return render(request, 'product_form.html', {'form': form})


def update_product(request, id):
    prod = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=prod)

    if form.is_valid():
        form.save()
        return redirect('list')

    return render(request, 'product_form.html', {'form': form, 'product': prod})


def delete_product(request, id):
    prod = Product.objects.get(id=id)
    if request.method == 'POST':
        prod.delete()
        return redirect('list')

    return render(request, 'prod-del-confirm.html', {'product': prod})
