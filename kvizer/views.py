from django.shortcuts import render, redirect
from .forms import KvizForm, PitanjeForm, RegisterForm
from .models import Pitanje, Odgovor, Kviz, User, Rezultat
from .my_functions import get_pitanja_sa_odgovorima, broj_bodova_procenti
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError


def home_kviz(request):
    return render(request, 'kvizer/home_kviz.html')

# ovde sam dodao 'broj' da bi mogao da odredim sta da mi se prikazuje na stranici


@login_required(login_url='/login/')
def kvizovi(request, broj):
    razred = User.get_godina(request.user)
    svi_kvizovi = Kviz.objects.filter(
        godina=razred).order_by('godina')
    najnoviji_kvizovi = Kviz.objects.filter(
        godina=razred).order_by('-id')[:10]
    return render(request, 'kvizer/kvizovi.html', {'svi_kvizovi': svi_kvizovi,
                                                   'najnoviji_kvizovi': najnoviji_kvizovi,
                                                   'broj': broj})


@login_required(login_url='/login/')
def create_kviz(request):
    if request.method == "POST":
        korisnik = User.objects.get(pk=4)
        print(korisnik.id)
        form = KvizForm(request.POST)
        if form.is_valid():
            get_naziv = form.cleaned_data["naziv"]
            get_predmet = form.cleaned_data["predmet"]
            get_godina = form.cleaned_data["godina"]
            get_trajanje_kviza = form.cleaned_data["trajanje_kviza"]
            novi_kviz = Kviz(naziv=get_naziv, predmet=get_predmet, godina=get_godina,
                             id_korisnika_id=korisnik.id, trajanje_kviza=get_trajanje_kviza)
            novi_kviz.save()
            return redirect('create_answers', id_kviza=novi_kviz.id)
    else:
        form = KvizForm()

    return render(request, 'kvizer/create_kviz.html', {'form': form})


@login_required(login_url='/login/')
def create_answers(request, id_kviza):
    if request.method == "POST":
        form = PitanjeForm(request.POST)
        if form.is_valid():
            get_pitanje = form.cleaned_data["Pitanje"]
            get_tacan_odgovor = form.cleaned_data["Tacan_odgovor"]
            get_netacan_odgovor1 = form.cleaned_data["Netacan_odgovor1"]
            get_netacan_odgovor2 = form.cleaned_data["Netacan_odgovor2"]
            get_netacan_odgovor3 = form.cleaned_data["Netacan_odgovor3"]

            id_from_kviz = Kviz.objects.get(pk=id_kviza)
            pitanje = Pitanje(id_kviza=id_from_kviz,
                              pitanje=get_pitanje)
            pitanje.save()
            id_from_pitanje = Pitanje.objects.get(pk=pitanje.pk)
            Tacan_odgovor = Odgovor(id_pitanja=id_from_pitanje,
                                    odgovor=get_tacan_odgovor,
                                    tacnost=1)
            Tacan_odgovor.save()
            Netacan_odgovor1 = Odgovor(id_pitanja=id_from_pitanje,
                                       odgovor=get_netacan_odgovor1,
                                       tacnost=0)
            Netacan_odgovor1.save()
            if get_netacan_odgovor2:
                Netacan_odgovor2 = Odgovor(id_pitanja=id_from_pitanje,
                                           odgovor=get_netacan_odgovor2,
                                           tacnost=0)
                Netacan_odgovor2.save()
            if get_netacan_odgovor3:
                Netacan_odgovor3 = Odgovor(id_pitanja=id_from_pitanje,
                                           odgovor=get_netacan_odgovor3,
                                           tacnost=0)
                Netacan_odgovor3.save()
            return redirect('create_answers', id_kviza=id_kviza)
    else:
        form = PitanjeForm()

    return render(request, 'kvizer/create_answers.html', {'form': form})


@login_required(login_url='/login/')
def start_kviz(request, id_kviza):
    kviz = Kviz.objects.get(id=id_kviza)
    pitanja_odgovori = get_pitanja_sa_odgovorima(id_kviza)
    if request.method == "POST":
        broj_bodova = broj_bodova_procenti(request, pitanja_odgovori)
        try:
            rezultat = Rezultat(bodovi=broj_bodova,
                                id_korisnika_id=request.user.id,
                                id_kviza_id=id_kviza
                                )
            rezultat.save()
        except IntegrityError:
            messages.warning(
                request, 'Ne mozete dva puta da radite isti kviz')
            return redirect('home_kviz')
        return redirect('end_kviz', bodovi=broj_bodova)
    return render(request, 'kvizer/start_kviz.html', {'pitanja_odgovori': pitanja_odgovori,
                                                      'kviz': kviz})


def end_kviz(request, bodovi):
    return render(request, 'kvizer/end_kviz.html', {'bodovi': bodovi})


@login_required(login_url='/login/')
def profile(request):
    if request.user.tip == "Profesor":
        sta_sad = 'sta sad'
    else:
        sta_sad = 'ucenik'
    return render(request, 'kvizer/profile.html', {'form': sta_sad})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            ime = form.cleaned_data['ime']
            prezime = form.cleaned_data['prezime']
            messages.success(
                request, f'Korisnik "{ime} {prezime}"  je uspesno napravio nalog! ')

            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'kvizer/register.html', {'form': form})
