from celery import shared_task
from django.contrib.auth import get_user_model
from django.db import transaction

from .selectors import *
from ..inventories.models import InventoryItem, Inventory

User = get_user_model()


@shared_task
def submit_offer():
    with transaction.atomic():
        find_active_offers()
        buyer_offers = find_buy_offer()
        seller_offers = find_sell_offer()
        for buyer_offer in buyer_offers:
            for seller_offer in seller_offers:
                if buyer_offer.item == seller_offer.item and buyer_offer.user != seller_offer.user:
                    if buyer_offer.user.deposit >= buyer_offer.price >= seller_offer.price:
                        _min_quantity = min(buyer_offer.quantity, seller_offer.quantity)
                        price = seller_offer.price * _min_quantity
                        create_trade(buyer_offer.item, seller_offer.user, buyer_offer.user,
                                     seller_offer, _min_quantity, buyer_offer)

                        if not InventoryItem.objects.filter(user=buyer_offer.user, item=buyer_offer.item).exists():
                            inventory = Inventory.objects.get(user=buyer_offer.user)
                            item = InventoryItem.objects.create(item=buyer_offer.item,
                                                                user=buyer_offer.user)
                            inventory.inv_items.add(item)

                        buyer_inventory_item = InventoryItem.objects.get(user=buyer_offer.user,
                                                                         item=buyer_offer.item.id)
                        seller_inventory_item = InventoryItem.objects.get(user=seller_offer.user,
                                                                          item=seller_offer.item.id)

                        change_seller_offer_quantity(seller_offer, _min_quantity)
                        change_buyer_offer_quantity(buyer_offer, _min_quantity)

                        change_users_deposit(buyer_offer.user, seller_offer.user, price)

                        change_item_quantity(buyer_inventory_item, seller_inventory_item, _min_quantity)

                        buyer_offer_check(buyer_offer)
                        seller_offer_check(seller_offer)


submit_offer.delay()
