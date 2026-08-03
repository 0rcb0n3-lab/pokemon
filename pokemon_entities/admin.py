from django.contrib import admin

# Register your models here.
from .models import Pokemon, PokemonEntity


admin.site.register(Pokemon)
admin.site.register(PokemonEntity)

