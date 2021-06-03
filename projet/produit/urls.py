from django.urls import path
from . import views

name = 'acceuil'
urlpatterns = [
    path('', views.homeproduct, name='acceuil'),
]
