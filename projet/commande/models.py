from django.db import models
from client.models import Client
from produit.models import Produit

# Create your models here.


class Commande(models.Model):
    STATUS = (
        ('en instance', 'en instance'),
        ('livré', 'livré'),
        ('non livré', 'non livré')
    )

    client = models.ForeignKey(
        Client, null=True, on_delete=models.CASCADE)
    produit = models.ForeignKey(
        Produit, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_commande = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return "{}\t{}".format(self.client.nom, self.status)
