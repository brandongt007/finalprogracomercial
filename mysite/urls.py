from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include('pensum.urls')),
]
