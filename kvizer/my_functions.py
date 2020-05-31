
from .models import Pitanje, Odgovor, Rezultat
from django.db.models import Q
from random import shuffle


def get_pitanja_sa_odgovorima(id_kviza):
    pitanja = Pitanje.objects.filter(id_kviza_id=id_kviza)
    pitanja_odgovori = {}
    for pitanje in pitanja:
        odgovori = list(Odgovor.objects.filter(id_pitanja_id=pitanje.id))
        shuffle(odgovori)
        pitanja_odgovori[pitanje] = odgovori
    return pitanja_odgovori


def broj_bodova_procenti(request, pitanja_odgovori):
    tacni_odgovori = 0
    for pitanje in pitanja_odgovori:
        if str(pitanje.id) in request.POST:
            odgovor_id = request.POST[str(pitanje.id)]
            rezultat = Odgovor.objects.get(id=odgovor_id)
            if rezultat.tacnost:
                tacni_odgovori += 1
    if tacni_odgovori:
        return int(tacni_odgovori/len(pitanja_odgovori)*100)
    else:
        return 0


def add_result(request, kvizovi):
    for kviz in kvizovi:
        try:
            Rezultat.objects.get(Q(id_kviza_id=kviz['id'])
                                 & Q(id_korisnika_id=request.user.id))
            kviz['rezultat'] = True
        except Rezultat.DoesNotExist:
            kviz['rezultat'] = False
    return kvizovi


class Odgovori():
    def __init__(self, odgovori):
        self.tacan_odgovor = odgovori[0]
        self.netacan_odgovor1 = odgovori[1]
        if len(odgovori) == 3:
            self.netacan_odgovor2 = odgovori[2]
            self.netacan_odgovor3 = ''
        elif len(odgovori) == 4:
            self.netacan_odgovor2 = odgovori[2]
            self.netacan_odgovor3 = odgovori[3]
        else:
            self.netacan_odgovor2 = ''
            self.netacan_odgovor3 = ''

    def get_odgovori(odgovori):
        return Odgovori(odgovori)
