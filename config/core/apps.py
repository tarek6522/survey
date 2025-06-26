from django.apps import AppConfig

class CoreConfig(AppConfig):
    def ready(self):
        import config..signals
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'config.'
