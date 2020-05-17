from django.shortcuts import render
from .liga_rezultati import Liga, ProvajderPodataka
from .my_functions import UtakmiceKola, Provajder
from .models import Sudija, Delegat, Sezona, TimoviSokobanja, ClanOdbora, Odbor, Obavestenja, Propisi, Vest, Slika, Video
from django.db.models import Q
from django.views.generic import ListView, DetailView


def home(request):
    vesti = Vest.objects.all()[:3]
    slike = Slika.objects.exclude(vest_id__isnull=False)[:3]
    return render(request, "fudbal/home.html", {"vesti": vesti, "slike": slike})


def savez(request):
    return render(request, "fudbal/o_savezu.html")


def rukovodstvo(request):
    clanovi_rukovodstava = ClanOdbora.objects.filter(
        odbor_id__naziv_odbora='Rukovodstvo')
    return render(request, "fudbal/rukovodstvo.html", {'clanovi': clanovi_rukovodstava})


def odbori(request):
    odbori = Odbor.objects.filter(~Q(naziv_odbora='Rukovodstvo'))
    clanovi_po_odborima = []
    for odbor in odbori:
        clanovi_odbora = ClanOdbora.objects.filter(
            odbor_id__naziv_odbora=odbor.naziv_odbora)
        clanovi_po_odborima.append(clanovi_odbora)
    return render(request, "fudbal/odbori.html", {'odbori': clanovi_po_odborima})


def propisi(request):
    propisi = Propisi.objects.all()
    return render(request, "fudbal/propisi.html", {"propisi": propisi})


def liga_rezultati(request):
    poslednja_sezona_obj = Sezona.objects.all().order_by('-sezona').first()
    poslednja_sezona = poslednja_sezona_obj.sezona
    liga = UtakmiceKola(Provajder())
    utakmice_po_kolima = liga.dohvati_kola(poslednja_sezona, 'LIGA')
    trenutna_sezona = "{}/{}".format(poslednja_sezona_obj.sezona,
                                     poslednja_sezona_obj.sezona + 1)
    return render(
        request,
        "fudbal/liga_rezultati.html",
        {"utakmice_po_kolima": utakmice_po_kolima, "sezona": trenutna_sezona},
    )


def liga_tabela(request):
    poslednja_sezona = Sezona.objects.all().order_by('-sezona').first().sezona
    poslednja_sezona_obj = Sezona.objects.get(
        Q(sezona=poslednja_sezona) & Q(tip_id__tip="LIGA"))
    liga = Liga(ProvajderPodataka())
    tabela_utakmica = liga.tabela(poslednja_sezona_obj)
    return render(request, "fudbal/liga_tabela.html", {"timovi": tabela_utakmica})


def kup_rezultati(request):
    return render(request, "fudbal/kup_rezultati.html")


def kup_tabela(request):
    return render(request, "fudbal/kup_tabela.html")


def delegiranje_sudija(request):
    poslednja_sezona_obj = Sezona.objects.all().order_by('-sezona').first()
    poslednja_sezona = poslednja_sezona_obj.sezona
    liga = UtakmiceKola(Provajder())
    utakmice_po_kolima = liga.dohvati_kola(poslednja_sezona, 'LIGA')
    trenutna_sezona = "{}/{}".format(poslednja_sezona_obj.sezona,
                                     poslednja_sezona_obj.sezona + 1)
    return render(
        request,
        "fudbal/delegiranje_sudija.html",
        {"utakmice_po_kolima": utakmice_po_kolima, "sezona": trenutna_sezona},
    )


def lista_sudija(request):
    sudije = Sudija.objects.all()
    return render(request, "fudbal/lista_sudija_delegata.html", {"sudije": sudije})


def lista_delagata(request):
    delegati = Delegat.objects.all()
    return render(request, "fudbal/lista_sudija_delegata.html", {"sudije": delegati})


def obavestenja(request):
    obavestenja = Obavestenja.objects.all()

    return render(request, "fudbal/obavestenja.html", {"obavestenja": obavestenja})


def timovi_sokobanje(request):
    ucesca = TimoviSokobanja.objects.values('ucesce').distinct()
    timovi_sokobanje = {}
    for ucesce in ucesca:
        liga = ucesce['ucesce']
        timovi_u_ligi = TimoviSokobanja.objects.filter(ucesce=liga)
        timovi_sokobanje[liga] = timovi_u_ligi
    return render(request, "fudbal/timovi_sokobanje.html", {"lige": timovi_sokobanje})


class VestiListView(ListView):
    context_object_name = "vesti"
    paginate_by = 4
    queryset = Vest.objects.all()


class VestDetailView(DetailView):
    queryset = Vest.objects.all()

    def get_context_data(self, **kwargs):
        context = super(VestDetailView, self).get_context_data(**kwargs)
        context['videi'] = Video.objects.all()
        context['slike'] = Slika.objects.all()

        return context


class GalleryListView(ListView):
    model = Slika
    context_object_name = "slike"
    paginate_by = 6
    queryset = Slika.objects.exclude(vest_id__isnull=False)
