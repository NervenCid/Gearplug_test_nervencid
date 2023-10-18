#importamos las librerias del sistema
from __future__ import absolute_import, unicode_literals
import os

#Importasmos el 'celery'
from celery import Celery
from celery.schedules import crontab

#Establecemos la variable de entorno DJANGO_SETTINGS_MODULE para que Celery pueda encontrar tu configuración de Django.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Gearplug.settings')

#Creamos la aplicacion con el proyecto
app = Celery('Gearplug')

# Carga la configuración de Celery desde tu archivo de configuración Django (settings.py).
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descubre y registra automáticamente tareas en tu aplicación Django.
app.autodiscover_tasks()

#
'''
app.conf.beat_schedule = {
    'Tarea_periodica': {
        'task': 'Poketasks.tasks.create_random_pokemon',        
        'schedule': 2.0,
        'args': ()
    },
}
'''
app.conf.timezone = 'UTC'

@app.task
def test(arg):
    print(arg)

@app.task
def add(x, y):
    z = x + y
    print(z)