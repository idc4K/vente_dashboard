from django.forms import ModelForm
from .models import Commande


class CommandForm(ModelForm):

    class Meta:
        model = Commande
        fields = '__all__'
