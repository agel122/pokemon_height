from django.urls import path

from .views import pokelistview, delete_pokemon

urlpatterns = [
    path('', pokelistview, name='pokelist'),
    path('delete/<str:pokemon>/', delete_pokemon, name='delete_pokemon')
]
