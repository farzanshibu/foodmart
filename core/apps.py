from django.apps import AppConfig
from django_web_components import component


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"

    def ready(self):
        # Implicitly register components decorated with @component.register
        from . import components
