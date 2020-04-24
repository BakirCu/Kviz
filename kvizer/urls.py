from django.urls import path
from . import views


urlpatterns = [
    path('', views.create_kviz, name='create_kviz'),

]
