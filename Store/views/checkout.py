
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

API = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/');

# utility function
def cal_total_pay_amt(cart):
    total = 0
    for c in cart:
        discount = c.get('tshirt').discount
        price = c.get('size').Price
        sale_price = floor(price - ( price * (discount/100) ))
        total_of_single_product = sale_price * c.get('quantity')
        total = total + total_of_single_product
    
    return total


# --------------------------checkout page start -------------------------
@login_required(login_url = '/login/')
def checkout(request):
    # for GET request
    if request.method == 'GET':
        form = CheckoutForm()
        cart = request.session.get('cart')
        if cart is None:
            cart = []
        
        for c in cart:
            size_str = c.get('size')
            tshirt_id = c.get('tshirt')
            size_obj = SizeVarient.objects.get(size = size_str, Tshirt = tshirt_id)
            c['size'] = size_obj
            c['tshirt'] = size_obj.Tshirt
        
        print(cart)
        context = {
            'form': form,
            'cart': cart
        }
        return render(request, 'store/checkout.html', context=context)
    else:
        # For POST request
        form = CheckoutForm(request.POST)
        user = None
        if request.user.is_authenticated:
            user = request.user
        if form.is_valid():
            # payment
            cart = request.session.get('cart')
            if cart is None:
                cart = []
            for c in cart:
                size_str = c.get('size')
                tshirt_id = c.get('tshirt')
                size_obj = SizeVarient.objects.get(size = size_str, Tshirt = tshirt_id)
                c['size'] = size_obj
                c['tshirt'] = size_obj.Tshirt
            shipping_address = form.cleaned_data.get('shipping_address')
            phone = form.cleaned_data.get('phone')
            payment_method = form.cleaned_data.get('payment_method')
            total = cal_total_pay_amt(cart)
            print(shipping_address, phone, payment_method, total)
            order = Order()
            order.shipping_address = shipping_address
            order.phone = phone
            order.payment_method = payment_method
            order.total = total
            order.order_status = "PENDING"
            order.user = user
            order.save()
            print(order.id)

            #saving order items

            for c in cart:
                order_item = OrderItem()
                order_item.order = order
                size = c.get('size')
                tshirt = c.get('tshirt')
                order_item.price = floor(size.Price - ( size.Price * (tshirt.discount/100) ))
                order_item.quantity = c.get('quantity')
                order_item.size = size
                order_item.tshirt = tshirt
                order_item.save()


            #creating payment
            response = API.payment_request_create(
            amount=order.total,
            purpose='Payment For Tshirts',
            send_email=True,
            buyer_name= f'{user.first_name} {user.last_name}',
            email=user.email,
            redirect_url="http://localhost:8000/validate_payment"
            )
            
            print(response['payment_request'])
            payment_request_id = response['payment_request']['id']
            url = response['payment_request']['longurl']

            payment = Payment()
            payment.order = order
            payment.payment_request_id = payment_request_id
            payment.save()
            return redirect(url)
        else:
            return redirect('/checkout/')


# --------------------------checkout page end -------------------------

