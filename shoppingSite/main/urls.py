
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('productDetails/', views.productDetails,name='productDetails'),
    path('shop/', views.shop,name='shop'),
    path('cart/', views.cart,name='cart'),
    path('checkout/', views.checkout,name='checkout'),
]
