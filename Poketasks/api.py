#Importamos el modelo
from .models import Pokemon

#Importamos las liberias de django-framework
from rest_framework import viewsets, permissions, status

#Importamos el serializador
from .serializers import PokemonSerializer

#Importamos las configuraciones principales
from django.conf import settings

#Importamos la respuesta
from rest_framework.response import Response

#
from rest_framework.request import Request

#Creamos el viewset que contendra las consultas
class PokemonViewSet(viewsets.ModelViewSet):

    #Declaramos el conjunto de datos
    queryset = Pokemon.objects.all()

    #Declaramos los permisos
    permission_classes = [
        permissions.AllowAny
    ]
    #Indicamos el serializador
    serializer_class = PokemonSerializer

    # Anula los métodos que no se necesitan y los desactiva
    def create(self, request, *args, **kwargs):

        data = request.data
        campo_unico = data.get('pokemon_id')  # Reemplaza 'campo_unico' por el nombre del campo que deseas verificar

        if Pokemon.objects.filter(pokemon_id=campo_unico).exists():
            return Response({'message': 'El dato ya existe'}, status=status.HTTP_400_BAD_REQUEST)

        # Si los datos no existen, continuar con la creación        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
                
        return Response({'message': 'Operación de creación personalizada completada'}, status=status.HTTP_201_CREATED)

    #Bloqueamos el metodo PUT
    def update(self, request, *args, **kwargs):
        return Response({'message': 'Operación PUT deshabilitada'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    #Bloqueamos el metodo PATCH
    def partial_update(self, request, *args, **kwargs):
        return Response({'message': 'Operación PATCH deshabilitada'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    #Bloqueamos el metodo DELETE
    '''
    def destroy(self, request, *args, **kwargs):
        return Response({'message': 'Operación DELETE deshabilitada'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        '''
    