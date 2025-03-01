from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.faz_login, name='login'),
    path('registrar/', views.se_registra, name='registrar'),
    path('logout/', views.faz_logout, name='logout'),
]  