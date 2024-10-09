from django.contrib import admin
from .models import *
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'total_items')
    list_display_links = ('id', 'user_id')
    list_filter = ('user_id',)
    
    search_fields = ('author',)
    list_per_page = 25
admin.site.register(Cart, CartAdmin)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'course')
    list_display_links = ('id', 'cart', 'product', 'course')
    list_filter = ('cart','product', 'course')
    
    search_fields = ('author','product', 'course')
    list_per_page = 25
admin.site.register(CartItem, CartItemAdmin)
