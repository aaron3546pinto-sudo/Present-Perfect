from django.urls import include, path

from Qpage import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('userlogin.html', views.user_login, name='userlogin'),
    path('myorder.html', views.my_orders, name='adminlogin'),
    path('mycart.html', views.my_cart, name='mycart'),
    path('home.html',views.home,name='home'),
    path('categories.html',views.categories,name='categories'),
    path('categories1.html',views.categories1,name='categories'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('login/', views.login_view, name='login'),  # User login URL
    path('myorder/',views.my_orders,name='my orders'),
    path('checkout/',views.checkout,name='checkout'),
    path('process_checkout/',views.process_checkout,name='process_checkout'),
    path('userregistration.html',views.user_registration,name='user registration'),
    path('register/', views.register, name='register'),
]