from django.urls import path
from django.conf.urls import url
from my_app import views

urlpatterns = [
    url(r'about', views.about, name="about"),
    url(r'base', views.base, name="base"),
    url(r'index', views.index, name="index")
]

