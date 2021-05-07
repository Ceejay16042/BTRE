from django.conf.urls import url
from . import views

urlpatterns = [
    url('contact', views.contacts, name="contact")
    ]