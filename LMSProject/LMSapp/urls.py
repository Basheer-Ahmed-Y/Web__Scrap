# from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.home, name='home-page'),
    url(r'^s/$', views.search, name='search'),
    url(r'/$', views.empty, name='empty'),
    path('addcart', views.addcart, name='addcart'),
    path('checkout', views.checkout, name='checkout')
]