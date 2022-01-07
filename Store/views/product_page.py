
from django.shortcuts import render, HttpResponse, redirect
from Store.forms.authforms import CustomerCreationForm , CustomerAuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as userlogin, logout as lgout
from Store.models import Order, SizeVarient, Tshirt, Cart, OrderItem, Payment,Occasion,Brand,Color,IdealFor,NeckType,Sleeve
from math import floor
from django.contrib.auth.decorators import login_required
from Store.forms.checkout_form import CheckoutForm
from instamojo_wrapper import Instamojo
from Tshop.settings import API_KEY, AUTH_TOKEN


# ------------------------------show product start-----------------

def show_product(request, slug):
    tshirt = Tshirt.objects.get(slug=slug)
    size = request.GET.get('size')

    if size is None:
        size = tshirt.sizevarient_set.all().order_by('Price').first()
    else:
        size = tshirt.sizevarient_set.get(size = size)
    size_price = size.Price
    sell_price = floor(size_price - (size_price*(tshirt.discount/100)))

    context = {
        'tshirt' : tshirt,
        'price' : size_price,
        'sell_price' : sell_price,
        'active_size' : size
    }

    return render(request,template_name='store/product_info.html',context=context)

# ------------------------------show product end-----------------
