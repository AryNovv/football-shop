from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Produk


def show_main(request):
    product_list = Produk.objects.all()

    context = {
        'npm' : '2406495590',
        'name': 'Arya Novalino Pratama',
        'class': 'PBP B',
        'product_list': product_list
    }

    return render(request, "main.html", context)

def create_listing(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_listing.html", context)

def show_catalog(request, id):
    products = get_object_or_404(Produk, pk=id)
    products.increment_views()

    context = {
        'products': products
    }

    return render(request, "product_detail.html", context)