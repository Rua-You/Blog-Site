from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register_view, name='register'),
    path('login', views.login_view, name='login'),
    path('forgot-password', views.forgot_password, name='forgot_password'),
    path('reset-password', views.reset_password, name='reset_password'),
    path('map', views.map, name='map'),
    path('verifyaccount', views.verify_account, name='verify_account'),
    path('logout', views.logout_view, name='logout'),
    path('profile/<str:slug>', views.profile, name='profile'),
    path('profile/<int:id>/edit', views.edit_profile, name='edit_profile'),
    path('database', views.database, name='database'),
]