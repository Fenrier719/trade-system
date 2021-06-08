from rest_framework import serializers
from trade_system.inventories.models import Inventory, InventoryItem
from trade_system.items.api.serializers import ItemSerializer
from trade_system.users.api.serializers import UserSerializer


class InventorySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    inv_items = ItemSerializer()

    class Meta:
        model = Inventory
        fields = (
            'user',
            'inv_items',
        )


class InventoryListSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = InventoryItem
        fields = (
            'item',
            'quantity',
        )
