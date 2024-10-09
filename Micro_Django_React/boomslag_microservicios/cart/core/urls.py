
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('api/cart/', include('apps.cart.urls')),
   path('admin/', admin.site.urls),
   ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
