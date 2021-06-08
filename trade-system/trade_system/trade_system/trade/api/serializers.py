from items.api.serializers import ItemSerializer
from offers.api.serializers import OfferSerializer
from rest_framework import serializers
from trade.models import Trade
from users.api.serializers import UserSerializer


class TradeSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    seller = UserSerializer()
    buyer = UserSerializer()
    seller_offer = OfferSerializer()
    buyer_offer = OfferSerializer()

    class Meta:
        model = Trade
        fields = (
            'item',
            'seller',
            'buyer',
            'seller_offer',
            'quantity',
            'buyer_offer',
            'description',
        )
