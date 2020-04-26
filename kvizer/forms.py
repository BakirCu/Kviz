from django.forms import ModelForm
from .models import Kviz


class KvizForm(ModelForm):
    class Meta:
        model = Kviz
        fields = ['naziv', 'predmet', 'godina',
                  'trajanje_kviza', 'id_korisnika']
