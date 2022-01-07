
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
from django.core.paginator import Paginator
from urllib.parse import urlencode

def index(request):

    query = request.GET
    tshirts = []
    tshirts = Tshirt.objects.all()

    brand = query.get('brands')
    neckType = query.get('necktype')
    occasion = query.get('occasion')
    colors = query.get('colors')
    idlefor = query.get('idlefor')
    sleevs = query.get('sleevs')
    page = query.get('page')

    if (page is not None or page == ''):
        page == 1


    if brand != '' and brand is not None:
        tshirts = tshirts.filter(Brand__slug = brand)
    if neckType != '' and neckType is not None:
        tshirts = tshirts.filter(neck_type__slug = neckType)
    if occasion != '' and occasion is not None:
        tshirts = tshirts.filter(occasion__slug = occasion)
    if colors != '' and colors is not None:
        tshirts = tshirts.filter(Color__slug = colors)
    if sleevs != '' and sleevs is not None:
        tshirts = tshirts.filter(Sleeve__slug = sleevs)
    if idlefor != '' and idlefor is not None:
        tshirts = tshirts.filter(ideal_for__slug = idlefor)

    occasions = Occasion.objects.all()
    brands = Brand.objects.all()
    colors = Color.objects.all()
    idlefor = IdealFor.objects.all()
    sleevs = Sleeve.objects.all()
    necktype = NeckType.objects.all()
    # tshirts = Tshirt.objects.all()
    # print(len(tshirts))
    # This loop loop converted into simple tag in templatetags file
    # for t in tshirts:
    #     min_price = t.sizevarient_set.all().order_by('Price').first()
    #     # print(t, min_price.Price, min_price.size)
    #     t.min_price = min_price.Price
    #     t.after_discount = t.min_price-(t.min_price*t.discount/100)
    #     t.after_discount = floor(t.after_discount)

    cart = request.session.get('cart')
    # print(cart)

    paginator = Paginator(tshirts, 3)
    page_object = paginator.get_page(page)

    query = request.GET.copy()
    query['page'] = ''
    pageurl = urlencode(query)

    context = {

        'page_object' : page_object,
        'occasions' : occasions,
        'brands' : brands,
        'colors' : colors,
        'idlefor' : idlefor,
        'sleevs' : sleevs,
        'necktype' : necktype,
        'pageurl' : pageurl

    }
    return render(request, template_name='store/index.html',context=context)
