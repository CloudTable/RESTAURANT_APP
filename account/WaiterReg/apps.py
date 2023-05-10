from django.apps import AppConfig


class WaiterregConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'WaiterReg'

    def ready(self):
        import WaiterReg.signals