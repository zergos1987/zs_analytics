from django.apps import AppConfig

class YourProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    
    def ready(self):
        # Import of singnal and other initialization code
        import app.signals