from django.apps import AppConfig


class PoketasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Poketasks'

    #Importamos las 'signals'
    def ready(self):
        from . import signals
