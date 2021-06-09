from rest_framework import serializers
from trade_system.items.api.serializers import ItemSerializer
from trade_system.users.api.serializers import UserSerializer
from trade_system.watchlists.models import Watchlist, WatchlistItem


class WatchlistItemSerialize(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = WatchlistItem
        fields = (
            'id',
            'item',
        )


class WatchListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Watchlist
        fields = [
            'watchlist_items',
            'user',
        ]


class ListWatchListSerializer(serializers.ModelSerializer):
    watchlist_items = ItemSerializer()

    class Meta:
        model = Watchlist
        fields = [
            'watchlist_items',
        ]
