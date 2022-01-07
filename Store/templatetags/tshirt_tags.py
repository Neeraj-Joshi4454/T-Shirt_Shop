from django import template
from math import floor
from Store.models import Tshirt

register = template.Library()



@register.filter
def rupee(number):
    # return f'&#8377;{number}'
    return f'₹{number}'



@register.simple_tag
def sitename(Tshirt):
    # return("Casual Mens Wear")
    return Tshirt.Brand

# ---------------tags for pricing in product_info page start------------------
@register.simple_tag
def min_price(Tshirt):
    size = Tshirt.sizevarient_set.all().order_by('Price').first()
    return size.Price


@register.simple_tag
def disamt(Tshirt):
    price = min_price(Tshirt)
    discount = Tshirt.discount
    dprice =price-price*discount/100
    return floor(dprice)


# ---------------tags for pricing in product_info page end------------------


@register.simple_tag
def get_active_size_button_class(active_size, size):
    
    if active_size == size:
        return "btn-dark"
    else:
        return "btn-light"


# ----------------simple tag for multiplication of price in cart page-----------------

@register.simple_tag
def multiply(a,b):
    return a*b


@register.simple_tag
def clc_sale_price(price, discount):
    return floor(price - ( price * (discount/100) ))

@register.filter
def cal_total_pay_amt(cart):
    total = 0
    for c in cart:
        discount = c.get('tshirt').discount
        price = c.get('size').Price
        sale_price = clc_sale_price(price, discount)
        total_of_single_product = sale_price * c.get('quantity')
        total = total + total_of_single_product
    
    return total




# ---------------------------Simple tag for order status-------------------------

@register.simple_tag
def get_order_status_class(status):
    if status == "COMPLETED":
        return "success"
    elif status == "PLACED":
        return "info"




# ---------------------------------tags for filter-------------------------

@register.simple_tag
def selected_attr(request_slug, slug):
    if request_slug == slug:
        return "selected"
    else:
        return ''