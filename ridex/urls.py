from django.contrib import admin
from django.urls import path
from ridex import views

urlpatterns = [
    path('', views.signin, name = 'signin' ),
    path('index', views.index, name = 'home' ),
    path('register', views.register, name = 'register' ),
    path('signin', views.signin, name = 'signin' ),
    path('logout', views.LogoutPage, name = 'logout' ),
    # path('info', views.info, name = 'info' ),
    path('payment', views.payment, name = 'payment' ),
    path('contact', views.contact, name = 'contact' ),
]
