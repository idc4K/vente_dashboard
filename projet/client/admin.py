from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'telephone', 'date_creation')
    search_fields = ['nom']
# Register your models here.


admin.site.register(Client, ClientAdmin)
