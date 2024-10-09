from django.contrib import admin
from . import models

@admin.register(models.Wallet)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_earnings', 'total_spent', 'address', )
    search_fields = ('user', 'total_earnings', 'total_spent', 'total_transfered',  'total_received', 'address', )