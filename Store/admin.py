from django.contrib import admin
from django.contrib.admin.decorators import register
from django.db.models.query_utils import RegisterLookupMixin
from Store.models import Cart, Payment, Order, OrderItem ,Brand, Color, IdealFor, NeckType, Occasion, SizeVarient, Sleeve, Tshirt
from django.utils.html import  format_html
# Register your models here.

class SizeVarientConfig(admin.TabularInline):
    model = SizeVarient

class OrderItemConfig(admin.TabularInline):
    model = OrderItem

class TshirtConfig(admin.ModelAdmin):
    inlines = [ SizeVarientConfig ]
    list_display = ['id','getimage','name', 'discount']
    list_editable = ['discount']
    sortable_by = ['name']
    list_filter = ['discount']
    list_display_links = ['name']
    list_per_page = 5
    def getimage(self, obj):
        # return obj.image.url
        return format_html(f'<a href="{obj.image.url}" target="_blank"><img width="50px" src="{obj.image.url}"/></a>')
        
class CartConfig(admin.ModelAdmin):
    model = Cart
    # fields = ('sizeVarient', 'quantity', 'user')
    list_display = ['quantity', 'size', 'tshirt', 'user', 'firstname', 'lastname']


    fieldsets = (
        ("Cart Info", { "fields": ('user', 'get_tshirt', 'get_sizeVarient', 'quantity') }),
    )

    readonly_fields = ('quantity', 'user', 'get_sizeVarient', 'get_tshirt')
    
    def get_tshirt(self, obj):
        tshirt = obj.sizeVarient.Tshirt
        tshirt_id = tshirt.id
        name = tshirt.name
        return format_html(f'<h1><a href="/admin/Store/tshirt/{tshirt_id}/change/" target="_blank">{name}</a></h1>')

    get_tshirt.short_description = 'Tshirt'


    def get_sizeVarient(self, obj):
        return obj.sizeVarient.size
    get_sizeVarient.short_description = "Size"

    def size(self, obj):
        return obj.sizeVarient.size

    def tshirt(self, obj):
        return obj.sizeVarient.Tshirt.name

    def firstname(self, obj):
        return obj.user.first_name

    def lastname(self, obj):
        return obj.user.last_name

class OrderConfig(admin.ModelAdmin):
    
    list_display = ['user', 'shipping_address', 'phone', 'date', 'order_status']
    list_filter = ['date']
    readonly_fields = ('user', 'phone', 'shipping_address', 'total', 'payment_method', 'payment', 'payment_request_id', 'payment_id','payment_status')

    fieldsets = (
        ("Order Information", {"fields": ('order_status', 'shipping_address', 'phone', 'total', 'user')}),

        ("Payment Information", {"fields": ('payment', 'payment_request_id', 'payment_id', 'payment_status')})
    )

    inlines = [OrderItemConfig]

    def payment_request_id(self, obj):
        return obj.payment_set.all()[0].payment_request_id

    def payment_status(self, obj):
        return obj.payment_set.all()[0].payment_status

    def payment_id(self, obj):
        payment_id = obj.payment_set.all()[0].payment_id
        if(payment_id is None or payment_id == ''):
            return "Payment ID is not available"
        else:
            return payment_id

    def payment(self, obj):
        payment_id = obj.payment_set.all()[0].id
        return format_html(f'<p><a href="/admin/Store/payment/{payment_id}/change/" target="_blank">Payment Information</a></p>')

admin.site.register(Tshirt,TshirtConfig)
admin.site.register(Occasion)
admin.site.register(IdealFor)
admin.site.register(NeckType)
admin.site.register(Sleeve)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Cart,CartConfig)
admin.site.register(Payment)
admin.site.register(Order,OrderConfig)
admin.site.register(OrderItem)
