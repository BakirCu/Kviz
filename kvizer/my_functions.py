
from .models import Pitanje, Odgovor


def get_pitanja_sa_odgovorima(id_kviza):
    pitanja = Pitanje.objects.filter(id_kviza_id=id_kviza)
    pitanja_odgovori = {}
    for pitanje in pitanja:
        odgovori = Odgovor.objects.filter(id_pitanja_id=pitanje.id)
        pitanja_odgovori[pitanje] = odgovori
    return pitanja_odgovori


def broj_bodova_procenti(request, pitanja_odgovori):
    tacni_odgovori = 0
    for pitanje in pitanja_odgovori:
        odgovor_id = request.POST.get(str(pitanje.id))
        rezultat = Odgovor.objects.get(id=odgovor_id)
        if rezultat.tacnost:
            tacni_odgovori += 1
    return int(tacni_odgovori/len(pitanja_odgovori)*100)
