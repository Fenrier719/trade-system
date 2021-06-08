from rest_framework import serializers

from trade_system.items.models import Item, Currency


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = (
            'code',
            'name',
        )


class ItemSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()

    class Meta:
        model = Item
        fields = (
            'id',
            'name',
            'code',
            'currency',
            'details',
        )
