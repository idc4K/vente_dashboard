from django.shortcuts import render
from django.http import HttpResponse
from client.models import Client
from commande.models import Commande
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='acces')
def homeproduct(request):
    client = Client.objects.all()
    commande = Commande.objects.all()
    context = {'clients': client, 'myorder': commande}

    return render(request, 'produit/produit_index.html', context)
    # return HttpResponse("Bienvenue sur la page des produits")
