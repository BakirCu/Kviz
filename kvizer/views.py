from django.shortcuts import render, redirect
from .forms import KvizForm


def create_kviz(request):
    if request.method == "POST":
        form = KvizForm(request.POST)
        if form.is_valid():
            return redirect('create_answers')
    else:
        form = KvizForm()

    return render(request, 'kvizer/create_kviz.html', {'form': form})


def create_answers(request):
    return render(request, 'kvizer/create_answers.html')
