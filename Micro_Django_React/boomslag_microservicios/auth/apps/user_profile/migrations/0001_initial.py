# Generated by Django 3.2.16 on 2024-08-21 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, default='media/users/user_default_profile.png', null=True, upload_to='media/users/pictures/', verbose_name='Picture')),
                ('banner', models.ImageField(blank=True, default='media/users/user_default_bg.jpg', null=True, upload_to='media/users/banners/', verbose_name='Banner')),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('url', models.CharField(blank=True, max_length=80, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('profile_info', models.TextField(blank=True, max_length=150, null=True)),
                ('facebook', models.CharField(blank=True, max_length=80, null=True)),
                ('twitter', models.CharField(blank=True, max_length=80, null=True)),
                ('instagram', models.CharField(blank=True, max_length=80, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=80, null=True)),
                ('youtube', models.CharField(blank=True, max_length=80, null=True)),
                ('github', models.CharField(blank=True, max_length=80, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
