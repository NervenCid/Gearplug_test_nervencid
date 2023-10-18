#Importamos la libreria
from celery import shared_task

from django.conf import settings

#Importamos el modulo para peticiones 'http'
import requests

#Importamos el modulo para generar numeros aleatorios
import random

#Declaramos la tarea
@shared_task
def create_random_pokemon():

    #Definimos la 'url' de 'pokeapi'
    pokeapi_url = 'https://pokeapi.co/api/v2/pokemon/'

    #Definimos la 'url' del 'api'
    api_url = 'http://localhost:8000/api/pokemon/'

    #Generamos un 'id' aleatorio
    random_pokemon_id = random.randint(1, 1292)

    # Realiza la solicitud GET
    response_pokeapi = requests.get(pokeapi_url+str(random_pokemon_id))

    # Verifica si la solicitud fue exitosa (código de estado 200)
    if response_pokeapi.status_code == 200:

        # Extrae los datos de la solicitud
        response_data = response_pokeapi.json()

        #A signamos los campos para la solicitud
        request_api_data = { 
            "pokemon_name" : response_data["name"], 
            "pokemon_id" : response_data["id"],
            "abilities" : response_data["abilities"]
        }

        #Realizamos la solicitud POST
        response_api = requests.post(api_url, json=request_api_data)  # Utilizamos json=data para enviar los datos en formato JSON

        # Verifica si la solicitud fue exitosa (código de estado 201)
        if response_api.status_code == 201:
            # Si la solicitud fue exitosa, retornamos los atributos
            return f"El Pokemon fue creado: {response_api.status_code} \n 'pokemon_name': {request_api_data['pokemon_name']}"
        elif response_api.status_code == 400:
            # Si el Pokemon ya existe, retornamos los atributos
            return f"El Pokemon ya existe: {response_api.status_code} \n 'pokemon_name': {request_api_data['pokemon_name']}"
        else:
            # Si la solicitud no fue exitosa, , retorna el código de estado
            return f"La solicitud a 'api' falló con el código de estado: {response_api.status_code}"                  
    
    else:
        # Si la solicitud no fue exitosa, retorna el código de estado
        return f"La solicitud a 'pokeapi' falló con el código de estado: {response_pokeapi.status_code}"
