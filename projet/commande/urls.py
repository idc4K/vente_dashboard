from django.urls import path
from . import views

urlpatterns = [
    path('', views.homecommande),
    path('ajout/', views.ajoutercommande, name='ajout'),
    path('modifier/<str:pk>', views.modifiercommande, name='modifier'),
    path('supprimer/<str:pk>', views.supprimercommande, name='supprimer'),
]
