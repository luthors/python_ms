# Generated by Django 3.2.16 on 2024-08-23 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_auto_20240822_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='address',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='private_key',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
