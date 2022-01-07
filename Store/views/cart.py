
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



def cart(request):
    cart = request.session.get('cart')
    if cart is None:
        cart = []
    
    for c in cart:
        tshirt_id = c.get('tshirt')
        tshirt = Tshirt.objects.get(id = tshirt_id)
        c['size'] = SizeVarient.objects.get(Tshirt = tshirt_id, size=c['size'])
        c['tshirt'] = tshirt

    context = {
        'cart': cart
    }

    print(cart)
    return render(request,template_name='store/cart.html', context=context)



# -----------------------------add to cart start ------------------

def add_to_cart(request, slug, size):
    user = None
    if request.user.is_authenticated:
        user = request.user

    cart = request.session.get('cart')
    
    if cart is None:
        cart = []

    tshirt = Tshirt.objects.get(slug = slug)
    size_temp = SizeVarient.objects.get(size = size, Tshirt = tshirt)
    flag = True
    for cart_obj in cart:
        t_id = cart_obj.get('tshirt')
        size_short = cart_obj.get('size')
        if t_id == tshirt.id and size == size_short:
            flag = False
            cart_obj['quantity'] = cart_obj['quantity']+1

    if flag:
        cart_obj = {
            'tshirt': tshirt.id,
            'size': size,
            'quantity': 1
        }
        cart.append(cart_obj)

    if user is not None:
            existing = Cart.objects.filter(user = user, sizeVarient = size_temp)
            if len(existing) > 0:
                obj = existing[0]
                obj.quantity = obj.quantity+1
                obj.save()

            else:
                c = Cart()
                c.user = user
                c.sizeVarient = size_temp
                c.quantity = 1
                c.save()

    
        

    request.session['cart'] = cart
    return_url = request.GET.get('return_url')
    return redirect(return_url)
# -----------------------------add to cart end ------------------