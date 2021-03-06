from django.urls import path
from . import views


urlpatterns = [path('', views.home_kviz, name='home_kviz'),
               path('create_kviz', views.create_kviz, name='create_kviz'),
               path('answers/<int:id_kviza>/',
                    views.create_answers, name='create_answers'),
               path('kvizovi', views.kvizovi, name='kvizovi'),
               path('start_kviz/<int:id_kviza>/',
                    views.start_kviz, name='start_kviz'),
               path('rezultati/<str:id_kviza>/',
                    views.rezultati, name='rezultati'),
               path('end_kviz/<str:bodovi>/', views.end_kviz, name='end_kviz'),
               path('register', views.register, name='register'),
               path('profile', views.profile, name='profile'),
               path('update_kviz/<str:id_kviza>/',
                    views.update_kviz, name='update_kviz'),
               path('update_answer/<str:id_kviza>/<str:id_pitanja>/',
                    views.update_answer, name='update_answer'),
               ]
