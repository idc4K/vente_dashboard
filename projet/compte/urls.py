from django.urls import path
from . import views


urlpatterns = [
    path('inscription', views.inscription, name='inscription'),
    path('acces', views.acces, name='acces'),
    path('quitter', views.logoutUser, name='quitter'),
]
