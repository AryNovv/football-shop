from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Produk
from django.http import HttpResponse
from django.core import serializers

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

def show_xml(request):
    product_list = Produk.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Produk.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, product_id):
    try:
        product_item = Produk.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product_item  = Produk.objects.get(pk=product_id)
        json_data = serializers.serialize("json", [product_item])
        return HttpResponse(json_data, content_type="application/json")
    except:
        return HttpResponse(status=404)