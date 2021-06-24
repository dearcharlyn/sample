# django_azure_demo/urls.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url('', include('foodtrackerapp.urls')),
    url('admin/', admin.site.urls),
]