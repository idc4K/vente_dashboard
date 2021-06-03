from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CommandForm
from .models import Commande
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='acces')
def homecommande(request):
    return render(request, 'commande/commande_index.html')


def ajoutercommande(request):
    form = CommandForm()

    if request.method == 'POST':
        form = CommandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'commande/ajouter_commande.html', context)


def modifiercommande(request, pk):
    commande = Commande.objects.get(id=pk)
    form = CommandForm(instance=commande)
    if request.method == 'POST':
        form = CommandForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'commande/ajouter_commande.html', context)


def supprimercommande(request, pk):
    commande = Commande.objects.get(id=pk)

    if request.method == 'POST':
        commande.delete()
        return redirect('/')

    context = {'item': commande}
    return render(request, 'commande/supprimer_commande.html', context)
