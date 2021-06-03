from django.contrib import admin
from .models import Commande


class CommandeAdmin(admin.ModelAdmin):
    list_display = ('client', 'produit', 'status', 'date_commande')
    search_fields = ['client']


# Register your models here.
admin.site.register(Commande, CommandeAdmin)
