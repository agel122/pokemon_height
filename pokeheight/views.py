from django.shortcuts import render, redirect
from .models import Pokemon
from .forms import PokemonForm
import requests
# import concurrent.futures
from django.db import IntegrityError


def pokelistview(request):
    message = ''
    if request.method == 'POST':
        form = PokemonForm(request.POST)
        if form.is_valid():
            pokemon_name = form.cleaned_data['pokemon_name']
            pokemon_height = requests.get(f"https://pokeapi.co/api/v2/pokemon/"
                                          f"{pokemon_name}").json()['height']
            try:
                Pokemon.objects.create(pokemon_name=pokemon_name, pokemon_height=pokemon_height)
                message = 'added'
            except IntegrityError:
                message = 'such pokemon already in the list, try another one'
    form = PokemonForm()
    pokemons = Pokemon.objects.order_by('pokemon_height').values()
    context = {
        'pokemon_names_heights': pokemons,
        'form': form,
        'message': message,
    }
    return render(request, 'pokelist.html', context)


def delete_pokemon(request, pokemon):
    Pokemon.objects.filter(pokemon_name=pokemon).delete()

    return redirect('pokelist')
