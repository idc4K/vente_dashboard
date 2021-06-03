from django.contrib import admin
from .models import Produit
from .models import Tag


class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', )
    search_fields = ['nom']


# Register your models here.
admin.site.register(Produit, ProduitAdmin)
admin.site.register(Tag)
