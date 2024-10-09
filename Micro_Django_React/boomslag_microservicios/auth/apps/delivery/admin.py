from django.contrib import admin
from .models import Address, UserAddresses

class UserAddressesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)
    list_display_links = ('id', 'user',)
    lis_per_page = 25
admin.site.register(UserAddresses, UserAddressesAdmin)

class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name','city', 'address_line_1', 'postal_zip_code')
    list_display_links = ('id', 'full_name', 'city', 'address_line_1', 'postal_zip_code')
    list_filter = ('full_name', 'city', 'address_line_1', 'postal_zip_code')
    search_fields = ('full_name', 'city', 'address_line_1', 'postal_zip_code')
    lis_per_page = 25
admin.site.register(Address, UserAddressAdmin)
