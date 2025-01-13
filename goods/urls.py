from django.contrib import admin
from django.urls import path

app_name = 'goods'

from goods import views

urlpatterns = [
    path('', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]