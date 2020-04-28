from django import forms
from .models import Kviz


class KvizForm(forms.ModelForm):
    class Meta:
        model = Kviz
        fields = ['id', 'naziv', 'predmet', 'godina',
                  'trajanje_kviza', 'id_korisnika']


class PitanjeForm(forms.Form):
    Pitanje = forms.CharField(label='Pitanje', max_length=200)
    Tacan_odgovor = forms.CharField(label='Tacan odgovor', max_length=200)
    Netacan_odgovor1 = forms.CharField(label='Netacan odgovor', max_length=200)
    Netacan_odgovor2 = forms.CharField(label='Netacan odgovor', max_length=200)
    Netacan_odgovor3 = forms.CharField(label='Netacan odgovor', max_length=200)
