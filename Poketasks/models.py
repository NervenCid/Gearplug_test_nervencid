#Importamos el modulo para modelos
from django.db import models
from django.forms import JSONField

#Esta clase contendra el modelo de las habilidades
'''
class Ability(models.Model):
    #A continuacion vienen las columnas de la tabla
    pokemonName = models.CharField(max_length=200)
    abilities = models.JSONField()
'''
    
#Esta clase contendra el modelo de un solo Pokemon
class Pokemon(models.Model):
    #A continuacion vienen las columnas de la tabla
    pokemon_name = models.CharField(max_length=200)
    pokemon_id = models.IntegerField()
    abilities = models.JSONField(blank=True, null=True)

