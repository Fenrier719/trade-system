from django.contrib.auth import get_user_model
from django.db import models

from trade_system.items.models import Item

User = get_user_model()


class WatchlistItem(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, blank=False, default=0, null=False, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return f'{self.item}'


class Watchlist(models.Model):
    watchlist_items = models.ManyToManyField(WatchlistItem, null=True)
    user = models.OneToOneField(User, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}s watchlist'
