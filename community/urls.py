from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register_view, name='register'),
    path('login', views.login_view, name='login'),
    path('map', views.map, name='map'),
    path('verifyaccount', views.verify_account, name='verify_account'),
    path('logout', views.logout_view, name='logout'),    
]