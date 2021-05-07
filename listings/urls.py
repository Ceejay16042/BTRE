from django.conf.urls import url
from django.urls import path

from listings import views


urlpatterns = [
    url(r'list', views.index, name="listings"),
    path('<int:listing_id>', views.Listing, name="listing"),
    url(r'search', views.search, name="search")
]

