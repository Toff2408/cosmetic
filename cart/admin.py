from django.contrib import admin
from .models import Shopcart, Payment, Shipping
# Register your models here.

@admin.register(Shopcart)
class ShopcartAdmin(admin.ModelAdmin):
    list_display = ['user','product','price','quantity','amount','cart_no','paid','created']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user' ,'total' ,'cart_no' ,'pay_code' ,'paid' ,'status' ,'created' ,'admin_note' ,'updated' ) 

@admin.register(Shipping)
class ShipingAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','phone','delivery_address','billing_address','city','state')

