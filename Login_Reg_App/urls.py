from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_reg),
    path('register', views.register),
    path('user/<int:poster_id>', views.profile),
    path('login', views.login),
    path('logout', views.logout),
    path('success', views.success),
]