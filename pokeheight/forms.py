from django.db import models
from django import forms
from .models import Pokemon


class PokemonForm(forms.Form):
        pokemon_name = forms.CharField(label='Name of pokemon', max_length=50)
