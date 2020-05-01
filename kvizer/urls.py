from django.urls import path
from . import views


urlpatterns = [
    path('', views.create_kviz, name='create_kviz'),
    path('answers/<str:id_kviza>/', views.create_answers, name='create_answers'),
    path('home_kviz', views.home_kviz, name='home_kviz'),
    path('start_kviz', views.start_kviz, name='start_kviz'),
    path('end_kviz', views.end_kviz, name='end_kviz'),
]
