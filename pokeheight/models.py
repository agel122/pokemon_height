from django.db import models


class Pokemon(models.Model):
    pokemon_name = models.CharField(max_length=30, unique=True)
    pokemon_height = models.SmallIntegerField()

    def __str__(self):
        return self.pokemon_name



