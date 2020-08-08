from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from user import views as user_views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='login.html'), name="logout"),
    path('', user_views.home, name="home"),

    path('contact/', user_views.contact, name='contact'),




]