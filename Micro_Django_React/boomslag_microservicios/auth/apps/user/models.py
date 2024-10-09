from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator
from slugify import slugify
from django.db.models.signals import post_save
import requests
from django.conf import settings
activecampaign_url = settings.ACTIVECAMPAIGN_URL
activecampaign_key = settings.ACTIVECAMPAIGN_API_KEY
from djoser.signals import  user_registered
import uuid, json
import stripe
stripe.api_key = settings.STRIPE_API_KEY
print('stripe api key', stripe.api_key)
from core.producer import producer
import json, uuid , re, os

pattern_special_characters = r'\badmin\b|[!@#$%^~&*()_+-=[]{}|;:",.<>/?]|\s'

def user_profile_directory_path(instance, filename):
    profile_pic_name = 'users/{0}/profile.jpg'.format(str(uuid.uuid4()))

def user_banner_directory_path(instance, filename):
    banner_pic_name = 'users/{0}/banner.jpg'.format(str(uuid.uuid4()))

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        def create_slug(username):
            if re.search(pattern_special_characters, username):
                raise ValueError('Username contains invalid characters')
            username = re.sub(pattern_special_characters, '', username)
            return slugify(username)
        email = self.normalize_email(email)
        extra_fields['slug'] = create_slug(extra_fields['username'])
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        #Send HTTP Request to Cart microservice containing the user data so cart microservice can create a cart for this user
        item={}
        item['id']=str(user.id)
        item['email']=user.email
        item['username']=user.username
        producer.produce( 
            'user_register',
            key="create_user",
            value=json.dumps(item).encode('utf-8')
        )
        producer.flush()
        print("*+"*100)
        print('user created', user)
        print("*+"*100)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.role="admin"
        user.verified=True
        user.become_seller=True
        user.save(using=self._db)

        return user
    

class UserAccount(AbstractBaseUser, PermissionsMixin):
    roles = (
        ('customer', 'Customer'),
        ('seller', 'Seller'),
        ('admin', 'Admin'),
        ('moderator', 'Moderator'),
        ('helper', 'Helper'),
        ('editor', 'Editor'),
    )

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    
    stripe_customer_id = models.CharField(max_length=100, blank=True, null=True)
    stripe_account_id = models.CharField(max_length=100, blank=True, null=True)
    stripe_payment_id = models.CharField(max_length=100, blank=True, null=True)

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_online = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    become_seller = models.BooleanField(default=False)
    agreed = models.BooleanField(default=False)

    role = models.CharField(max_length=10, choices=roles, default='customer')
    verified = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'agreed']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        counter = 1
        while UserAccount.objects.filter(slug=self.slug).exists():
            self.slug = f"{self.slug}-{counter}"
            counter += 1
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.email
    
def post_user_confirmed(request, user, *args,**kwargs):
    user=user
    stripe_customer = stripe.Customer.create(
        name=user.first_name + ' ' + user.last_name,
        email=user.email,
    )
    user.stripe_customer_id = stripe_customer['id']
    print('stripe customer id', user.stripe_customer_id)
    user.save()
    print('user saved', user)
    
    
    
    connect_account = stripe.Account.create(
        type="express",
        capabilities={"card_payments":{"requested": True}, "transfers":{"requested": True}}
    )
    print('connect_account', connect_account)
    user.stripe_account_id = connect_account['id']
    user.save()
    print("*"*100)
    
    
user_registered.connect(post_user_confirmed)