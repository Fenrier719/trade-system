from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "trade_system.users"

    def ready(self):
        import trade_system.users.signals
