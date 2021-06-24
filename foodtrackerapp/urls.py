# food/urls.py
from django.conf.urls import url
from foodtrackerapp  import views


urlpatterns = [
    url('', views.index, name='index'),
]