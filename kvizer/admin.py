from django.contrib import admin
from .models import Kviz, Pitanje, Odgovor, User

admin.site.register([Kviz, Pitanje, Odgovor, User])
