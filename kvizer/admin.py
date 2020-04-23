from django.contrib import admin
from .models import Kviz, Pitanje, Odgovor

admin.site.register([Kviz, Pitanje, Odgovor])
