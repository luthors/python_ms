from django.db import models
from djoser.signals import user_registered
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address')
    full_name = models.CharField(max_length=80, null=True, blank=True)
    address_line_1 = models.CharField(max_length=80, null=True, blank=True)
    address_line_2 = models.CharField(max_length=80, null=True, blank=True)
    city = models.CharField(max_length=80, null=True, blank=True)
    state_province_region = models.CharField(max_length=80, null=True, blank=True)
    postal_zip_code = models.CharField(max_length=80, null=True, blank=True)
    country_region = models.CharField(max_length=80, null=True, blank=True)
    telephone_number = models.CharField(max_length=80, null=True, blank=True)
    
    def __str__(self):
        return self.user.email
    
class UserAddresses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_address')
    address = models.ManyToManyField(Address)
    
def post_user_registered(request, user, *args, **kwargs):
    # Definir usuario que se registra
    user=user
    UserAddresses.objects.create(user=user)

user_registered.connect(post_user_registered)    

