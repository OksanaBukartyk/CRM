from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,  name='home'),
    path('about', views.about,  name='about'),

    path('buyers_list', views.buyers_list,  name='buyers_list'),
    path('sellers_list', views.sellers_list,  name='sellers_list'),
    path('products_list', views.products_list,  name='products_list'),
    path('sellings_list', views.sellings_list,  name='sellings_list'),

    path('buyer/edit/<int:id>', views.buyer_edit, name = 'buyer_edit'),
    path('seller/edit/<int:id>', views.seller_edit, name = 'seller_edit'),
    path('selling/edit/<int:id>', views.selling_edit, name = 'selling_edit'),
    path('product/edit/<int:id>', views.product_edit, name = 'product_edit'),

    path('buyer/delete/<int:id>/', views.buyer_delete, name='buyer_delete'),
    path('seller/delete/<int:id>/', views.seller_delete, name='seller_delete'),
    path('selling/delete/<int:id>/', views.selling_delete, name='selling_delete'),
    path('product/delete/<int:id>/', views.product_delete, name='product_delete'),

    path('buyer/create', views.buyer_create, name='buyer_create'),
    path('seller/create', views.seller_create, name='seller_create'),
    path('selling/create', views.selling_create, name='selling_create'),
    path('product/create', views.product_create, name='product_create'),

    path('user_sellings', views.user_sellings, name='user_sellings'),


]
