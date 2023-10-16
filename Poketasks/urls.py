#Importamos el modulo de enrutamiento
from rest_framework import routers

#Importamos el 'viewSet'
from .api import PokemonViewSet

#Instanciamos el enrutador
router = routers.DefaultRouter()

#Registramos las rutas
router.register('api/pokemons', PokemonViewSet, 'pokemon')

#Generamos las 'urls'
urlpatterns = router.urls
