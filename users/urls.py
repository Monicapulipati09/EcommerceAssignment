from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('shop/', views.shop, name="shop"),
    path('login/', views.login_req, name="login"),
    path('logout/', views.logout_req, name= "logout"),
    path('shop/add_to_cart/<int:product_id>/', views.add_to_cart, name="add_to_cart"),
    path('order_review/', views.order_review, name= "order_review"),
    path('', views.home, name="home"),
]

