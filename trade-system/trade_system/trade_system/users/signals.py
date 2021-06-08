from django.contrib.auth import get_user_model
from django.db.models import signals
from django.dispatch import receiver
from trade_system.watchlists.models import Watchlist
from trade_systme.inventories.models import Inventory

from . import models

User = get_user_model()


@receiver(signals.post_save, sender=models.User)
def post_save_user_signal(sender, instance, created, *args, **kwargs):
    if created:
        Watchlist.objects.create(user=instance)
        Inventory.objects.create(user=instance)
