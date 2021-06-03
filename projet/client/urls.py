from django.urls import path
from . import views

name = 'client'
urlpatterns = [
    path('<str:pk>', views.homeclient, name='client'),
]
