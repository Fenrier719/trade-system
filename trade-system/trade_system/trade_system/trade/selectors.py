from trade_system.offers.models import Offer

from trade_system.trade.models import Trade


def find_active_offers():
    return Offer.objects.filter(is_active=True)


def find_buy_offer():
    buy_offers = [offer for offer in list(find_active_offers()) if
                  offer.order_type == 1]
    return buy_offers


def find_sell_offer():
    sell_offers = [offer for offer in list(find_active_offers()) if
                   offer.order_type == 2]
    return sell_offers


def find_buyer():
    buyers = [buyer.user for buyer in list(find_buy_offer())]
    return buyers


def find_seller():
    sellers = [seller.user for seller in list(find_sell_offer())]
    return sellers


def change_item_quantity(buyer_item, seller_item, quantity):
    buyer_item.quantity = buyer_item.quantity + quantity
    buyer_item.save()
    seller_item.quantity = seller_item.quantity - quantity
    seller_item.save()


def change_users_deposit(buyer, seller, price):
    buyer.deposit -= price
    buyer.save()
    seller.deposit += price
    seller.save()


def create_trade(item, seller, buyer, seller_offer, quantity, buyer_offer):
    Trade.objects.create(item=item, seller=seller,
                         buyer=buyer, seller_offer=seller_offer,
                         quantity=quantity, buyer_offer=buyer_offer)


def change_seller_offer_quantity(seller_offer, quantity):
    seller_offer.quantity -= quantity
    seller_offer.save()


def change_buyer_offer_quantity(buyer_offer, quantity):
    buyer_offer.quantity -= quantity
    buyer_offer.save()


def buyer_offer_check(buyer_offer):
    if buyer_offer.quantity == 0:
        buyer_offer.is_active = False
        buyer_offer.save()


def seller_offer_check(seller_offer):
    if seller_offer.quantity == 0:
        seller_offer.is_active = False
        seller_offer.save()
