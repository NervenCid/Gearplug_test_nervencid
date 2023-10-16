#Importamos el modulo de 'serializers'
from rest_framework import serializers

#Importamos los modelos
from .models import Pokemon

#Creamos el serializer
class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('pokemonName', 'order', 'abilities')
        