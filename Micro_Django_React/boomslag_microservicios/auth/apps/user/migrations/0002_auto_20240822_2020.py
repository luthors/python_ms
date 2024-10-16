# Generated by Django 3.2.16 on 2024-08-23 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='become_seller',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='stripe_account_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='stripe_customer_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='stripe_payment_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='role',
            field=models.CharField(choices=[('customer', 'Customer'), ('seller', 'Seller'), ('admin', 'Admin'), ('moderator', 'Moderator'), ('helper', 'Helper'), ('editor', 'Editor')], default='customer', max_length=10),
        ),
    ]
