
from .models import Pitanje, Odgovor


def get_pitanja_sa_odgovorima(id_kviza):
    pitanja = Pitanje.objects.filter(id_kviza_id=id_kviza)
    pitanja_odgovori = {}
    for pitanje in pitanja:
        odgovori = Odgovor.objects.filter(id_pitanja_id=pitanje.id)
        pitanja_odgovori[pitanje] = odgovori
    return pitanja_odgovori
