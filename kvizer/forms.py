from django import forms
from .models import Kviz, User


class KvizForm(forms.ModelForm):
    class Meta:
        model = Kviz
        fields = ['id', 'naziv', 'predmet', 'godina',
                  'trajanje_kviza', ]


class KvizUpdateForm(forms.ModelForm):
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


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Lozinka', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Potvrdi lozinku', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'ime', 'prezime', 'tip', 'godina')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email je zauzet")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Lozinke se ne poklapaju")
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
