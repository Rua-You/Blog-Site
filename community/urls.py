from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('map', views.map, name='map'),
    # path('register', views.register),
    
]