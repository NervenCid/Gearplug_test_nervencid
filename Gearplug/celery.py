#importamos las librerias del sistema
import os

#Importasmos el 'celery'
from celery import Celery

#Establecemos la variable de entorno DJANGO_SETTINGS_MODULE para que Celery pueda encontrar tu configuración de Django.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Gearplug.settings')

#Creamos la aplicacion con el proyecto
app = Celery('Gearplug')

# Carga la configuración de Celery desde tu archivo de configuración Django (settings.py).
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descubre y registra automáticamente tareas en tu aplicación Django.
app.autodiscover_tasks()

# Configura Celery Beat para tareas periódicas
