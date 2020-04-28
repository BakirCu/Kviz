from django.shortcuts import render, redirect
from .forms import KvizForm, PitanjeForm
from .models import Pitanje, Odgovor, Kviz
from django.db.models import Q


def create_kviz(request):
    if request.method == "POST":
        form = KvizForm(request.POST)
        if form.is_valid():
            novi_kviz = form.save()
            return redirect('create_answers', id_kviza=novi_kviz.id)
    else:
        form = KvizForm()

    return render(request, 'kvizer/create_kviz.html', {'form': form})


def create_answers(request, id_kviza):
    if request.method == "POST":
        form = PitanjeForm(request.POST)
        if form.is_valid():
            get_pitanje = form.cleaned_data["Pitanje"]
            iff = Kviz.objects.get(pk=id_kviza)
            pitanje = Pitanje(id_kviza=iff, pitanje=get_pitanje)
            pitanje.save()
            print(pitanje.id)

            return redirect('create_answers', id_kviza=id_kviza)
    else:
        form = PitanjeForm()

    return render(request, 'kvizer/create_answers.html', {'form': form})
