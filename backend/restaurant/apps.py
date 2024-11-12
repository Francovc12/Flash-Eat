from django.apps import AppConfig


class RestaurantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restaurant'

    def ready(self):
        from .signals import assign_permissions