from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Produk
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  

    if filter_type == "all":
        product_list = Produk.objects.all()
    else:
        product_list = Produk.objects.filter(user=request.user)
        
    context = {
        'npm' : '2406495590',
        'name': 'Arya Novalino Pratama',
        'class': 'PBP B',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

def create_listing(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
        

    context = {'form': form}
    return render(request, "create_listing.html", context)

@csrf_exempt
@require_POST
def add_listing_entry_ajax(request):
    name = request.POST.get("name")
    description = request.POST.get("description")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    price = request.POST.get("price")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user

    new_produk = Produk(
        name=name, 
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        price=price,
        user=user
    )
    new_produk.save()

    return HttpResponse(b"CREATED", status=201)

@login_required(login_url='/login')
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
    data =[
        {
            'id': str(produk.id),
            'price': produk.price,
            'name': produk.name,
            'description': produk.description,
            'category': produk.category,
            'thumbnail': produk.thumbnail,
            'created_at': produk.created_at.isoformat() if Produk.created_at else None,
            'products_views' : produk.products_views,
            'is_featured': produk.is_featured,
            'is_product_hot' : produk.is_product_hot,
            'user_id': produk.user_id,

        }
        for produk in product_list

    ]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
        product_item = Produk.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        produk = Produk.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(produk.id),
            'price': produk.price,
            'name': produk.name,
            'description': produk.description,
            'category': produk.category,
            'thumbnail': produk.thumbnail,
            'created_at': produk.created_at.isoformat() if Produk.created_at else None,
            'products_views' : produk.products_views,
            'is_featured': produk.is_featured,
            'is_product_hot' : produk.is_product_hot,
            
            'user_id': produk.user_id,
            'user_username': produk.user.username if produk.user_id else None,

        }

        return JsonResponse(data)
    except  Produk.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)   

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_listing(request, id):
    prdk = get_object_or_404(Produk, pk=id)
    form = ProductForm(request.POST or None, instance=prdk)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_listing.html", context)

def delete_Listing(request, id):
    prdk = get_object_or_404(Produk, pk=id)
    prdk.delete()
    return HttpResponseRedirect(reverse('main:show_main'))