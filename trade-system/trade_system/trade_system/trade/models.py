from django.contrib.auth import get_user_model
from django.db import models

from trade_system.items.models import Item

from trade_system.offers.models import Offer

User = get_user_model()


class Trade(models.Model):
    item = models.ForeignKey(Item, blank=False, null=True, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, blank=False, null=False, on_delete=models.DO_NOTHING, related_name='seller_trade',
                               related_query_name='seller_trade')
    buyer = models.ForeignKey(User, blank=False, null=False, on_delete=models.DO_NOTHING, related_name='buyer_trade',
                              related_query_name='buyer_trade')
    seller_offer = models.ForeignKey(Offer, blank=False, null=False, on_delete=models.DO_NOTHING,
                                     related_name='seller_offer', related_query_name='seller_offer')
    buyer_offer = models.ForeignKey(Offer, blank=False, null=False, on_delete=models.DO_NOTHING,
                                    related_name='buyer_offer', related_query_name='buyer_offer')
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f'seller: {self.seller} | buyer: {self.buyer} | item: {self.item} | quantity: {self.quantity}'
