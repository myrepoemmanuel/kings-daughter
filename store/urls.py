from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name="shop_home"),
    path('', views.store, name="store"),
    path('store/nike/', views.nike, name="site-nike"),
    path('store/adidas/', views.adidas, name="site-adidas"),
    path('store/balenciaga/', views.balenciaga, name="site-balenciaga"),
    path('store/category/', views.dior, name="site-dior"),
    path('store/search/', views.search, name="searches"),


    
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('cart/update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('processContact/', views.processContact, name="processContact"),
]