from django.contrib.auth import get_user_model
from django.db import models

from trade_system.items.models import Item

User = get_user_model()


ORDER_TYPE = [(1, 'BUY'),
              (2, 'SELL')]


class Offer(models.Model):
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, blank=False, null=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='quantity')
    order_type = models.PositiveSmallIntegerField(choices=ORDER_TYPE)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user}s offer | item:{self.item} | quantity: {self.quantity} | status: {self.is_active}'

