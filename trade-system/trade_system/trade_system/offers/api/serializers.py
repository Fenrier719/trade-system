from rest_framework import serializers
from trade_system.inventories.models import InventoryItem
from trade_system.items.api.serializers import ItemSerializer

from trade_system.offers.models import Offer


class OfferCreateSerializer(serializers.ModelSerializer):

    def validate(self, data):
        user = self.context.get('request').user
        item = self.context.get('item')
        if data['order_type'] == 1 and data['price'] * data['quantity'] > user.deposit:
            raise serializers.ValidationError('Not enough money')
        elif data['order_type'] == 2:
            inv_item = InventoryItem.objects.get(item=item, user=user)
            if not inv_item:
                raise serializers.ValidationError('No such item in inventory')
            if data['quantity'] > inv_item.quantity:
                raise serializers.ValidationError('Not enough items in inventory')
        return data

    class Meta:
        model = Offer
        fields = (
            'quantity',
            'order_type',
            'price',
            'is_active',
        )


class OfferListSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = Offer
        fields = (
            'item',
            'quantity',
            'order_type',
            'price',
            'is_active',
        )
