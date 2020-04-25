from django.shortcuts import render


def create_kviz(request):
    return render(request, 'kvizer/create_kviz.html')


def create_answers(request):
    return render(request, 'kvizer/create_answers.html')
