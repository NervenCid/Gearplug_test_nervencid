#Importamos los modulos de 'django signals'
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

#Importamos los modelos
from .models import Pokemon

#
from django.core.mail import send_mail

#Declaramos el envio de email
@receiver(post_save, sender=Pokemon)
def send_email(sender, instance, created, **kwargs):
    
    if created:

        # Accedemos a los atributos del objeto que desencadeno la 'signal'
        pokemon_name = instance.pokemon_name
        pokemon_id = instance.pokemon_id
        abilities = instance.abilities

        #Definimos los parametros para el correo electronico
        subject = 'Pokemon nuevo creado: {}'.format(pokemon_name)
        message = 'Se ha creado un nuevo Pokemon!!\n Nombre: {0} \n ID: {1} \n Habilidades: {2}'.format(pokemon_name, pokemon_id, abilities)
        from_email =  settings.DEFAULT_FROM_EMAIL  # Debe coincidir con la dirección configurada en EMAIL_HOST_USER
        recipient_list = [settings.RECIPIENT_EMAIL]

        #Enviamos el email
        try:
            send_mail(subject, message, from_email, recipient_list)
            #return Response({'message': 'Correo electrónico enviado con éxito'}, status=status.HTTP_200_OK)
        except Exception as e:
            #return Response({'error en el envio de email': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            print('No se envio el correo electronico: ',  str(e))