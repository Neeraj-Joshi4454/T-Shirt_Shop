
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
from django.views.generic.base import View


class LoginView(View):
    def get(self, request):
        form = CustomerAuthenticationForm()

        next_page = request.GET.get('next')
        if next_page is not None:
            request.session['next_page'] = next_page

        context = {
            'form' : form
        }
        return render(request,template_name='store/login.html',context=context)


    def post(self, request):
        form = CustomerAuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if(user):
                userlogin(request, user)

                session_cart = request.session.get('cart')
                if session_cart is None:
                    session_cart = []
                else:
                    for c in session_cart:
                        size = c.get('size')
                        tshirt_id = c.get('tshirt')
                        quantity = c.get('quantity')
                        cart_obj = Cart()
                        cart_obj.sizeVarient = SizeVarient.objects.get(size = size, Tshirt = tshirt_id)
                        cart_obj.quantity = quantity
                        cart_obj.user = user
                        cart_obj.save()

                cart = Cart.objects.filter(user = user)
                session_cart = []
                for c in cart:
                   obj = {
                       'size': c.sizeVarient.size,
                       'tshirt': c.sizeVarient.Tshirt.id,
                       'quantity': c.quantity
                   }
                   session_cart.append(obj)

                request.session['cart'] = session_cart
                next_page = request.session.get('next_page')
                if next_page is None:
                        next_page = 'HomePage'
                return redirect(next_page)
        else:
            context = {
            'form' : form
            }
            return render(request,template_name='store/login.html',context=context)




# ---------------------login start----------------
# def login(request):

#     if request.method == 'GET':
#         form = CustomerAuthenticationForm()

#         next_page = request.GET.get('next')
#         if next_page is not None:
#             request.session['next_page'] = next_page

#         context = {
#             'form' : form
#         }
#         return render(request,template_name='store/login.html',context=context)

#     else:
#         form = CustomerAuthenticationForm(data = request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username = username, password = password)
#             if(user):
#                 userlogin(request, user)

#                 session_cart = request.session.get('cart')
#                 if session_cart is None:
#                     session_cart = []
#                 else:
#                     for c in session_cart:
#                         size = c.get('size')
#                         tshirt_id = c.get('tshirt')
#                         quantity = c.get('quantity')
#                         cart_obj = Cart()
#                         cart_obj.sizeVarient = SizeVarient.objects.get(size = size, Tshirt = tshirt_id)
#                         cart_obj.quantity = quantity
#                         cart_obj.user = user
#                         cart_obj.save()

#                 cart = Cart.objects.filter(user = user)
#                 session_cart = []
#                 for c in cart:
#                    obj = {
#                        'size': c.sizeVarient.size,
#                        'tshirt': c.sizeVarient.Tshirt.id,
#                        'quantity': c.quantity
#                    }
#                    session_cart.append(obj)

#                 request.session['cart'] = session_cart
#                 next_page = request.session.get('next_page')
#                 if next_page is None:
#                         next_page = 'HomePage'
#                 return redirect(next_page)
#         else:
#             context = {
#             'form' : form
#             }
#             return render(request,template_name='store/login.html',context=context)

# ---------------------login end----------------


# -----------------------signup start------------------

def signup(request):
    
    if(request.method == 'GET'):
        form = CustomerCreationForm()
        context = {
            "form" : form
        }
        return render(request,template_name='store/signup.html',context=context)
    else:
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.email = user.username
            user.save() 
            print(user)
            return redirect('login')
        context = {
            "form" : form
        }
        return render(request,template_name='store/signup.html',context=context)

# -----------------------signup start------------------


# -------------------logout start-----------------
def logout(request):
    # direct way to clear the sessions
    # request.session.clear()

    # another way to logout via inbuild method of django
    lgout(request)
    # return render(request,template_name='store/index.html')
    return redirect('HomePage')

# -------------------------Logout end-------------------
