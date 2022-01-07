
from django.contrib import admin
from django.urls import path

from Store.views import add_to_cart,checkout,show_product,cart, index, LoginView, logout, order, signup, validate_payment

urlpatterns = [
    
    path('', index,name="HomePage"),
    path('cart/',cart),
    path('login/',LoginView.as_view(), name='login'),
    path('order/',order, name='orders'),
    path('signup/',signup),
    path('logout/',logout),
    path('checkout/',checkout),
    path('product/<str:slug>',show_product),
    path('addtocart/<str:slug>/<str:size>',add_to_cart),
    path('validate_payment',validate_payment)

]
