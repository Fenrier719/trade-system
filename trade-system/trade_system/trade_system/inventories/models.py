from django.contrib.auth import get_user_model
from django.db import models

from trade_system.items.models import Item

User = get_user_model()


class InventoryItem(models.Model):
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, blank=False, null=False, default=0, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0, null=False)

    def __str__(self):
        return f'{self.user}s {self.item} | quantity: {self.quantity}'


class Inventory(models.Model):
    user = models.OneToOneField(User, blank=False, null=False, on_delete=models.CASCADE)
    inv_items = models.ManyToManyField(InventoryItem, null=True)

    def __str__(self):
        return f'{self.user}s inventory'
