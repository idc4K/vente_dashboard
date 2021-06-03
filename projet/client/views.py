from django.shortcuts import render
from django.http import HttpResponse
from .models import Client
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='acces')
def homeclient(request, pk):

    client = Client.objects.get(id=pk)
    commande = client.commande_set.all()
    commande_totale = commande.count()
    context = {'myclient': client, 'commande': commande,
               'commande_totale': commande_totale}
    return render(request, 'client/client_index.html', context)
