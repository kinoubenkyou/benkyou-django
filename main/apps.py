from django.apps import AppConfig
from django.conf import settings
from mongoengine import connect


class MainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main"

    def ready(self):
        return_ = super().ready()
        connect(**settings.MONGO)
        return return_
