from django.apps import AppConfig


class NoteswapMainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'NoteSwap_main'
from django.apps import AppConfig

class YourAppConfig(AppConfig):
    name = 'NoteSwap_main'

    def ready(self):
        import NoteSwap_main.signals  # Ensure signals are imported and connected
