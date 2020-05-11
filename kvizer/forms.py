from django import forms
from .models import Kviz, Korisnik


class KvizForm(forms.ModelForm):
    class Meta:
        model = Kviz
        fields = ['id', 'naziv', 'predmet', 'godina',
                  'trajanje_kviza', ]


class PitanjeForm(forms.Form):
    Pitanje = forms.CharField(label='Pitanje', max_length=200)
    Tacan_odgovor = forms.CharField(label='Tacan odgovor', max_length=200)
    Netacan_odgovor1 = forms.CharField(label='Netacan odgovor', max_length=200)
    Netacan_odgovor2 = forms.CharField(
        label='Netacan odgovor', max_length=200, required=False)
    Netacan_odgovor3 = forms.CharField(
        label='Netacan odgovor', max_length=200, required=False)


class RegistracijaForm(forms.ModelForm):
    lozinka = forms.CharField(max_length=32, min_length=5, widget=forms.PasswordInput(
        # ovo su opcije za ulepsavanje
        attrs={'class': 'form-control'}))

    class Meta:
        model = Korisnik
        fields = ['ime', 'prezime', 'tip', 'email', 'lozinka']


class LogovanjeForm(forms.Form):
    email = forms.EmailField()
    lozinka = forms.CharField(
        max_length=32, min_length=5, widget=forms.PasswordInput())
