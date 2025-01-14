from django.contrib import admin
from django.urls import path

app_name = 'goods'

from goods import views

urlpatterns = [
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]