from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from trade_system.watchlists.models import Watchlist, WatchlistItem
from rest_framework import response

from .serializers import ItemSerializer
from ..models import Item
from trade_system.offers.api.serializers import OfferCreateSerializer
from trade_system.watchlists.api.serializers import WatchListSerializer

User = get_user_model()


class ItemListViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Item.objects.all()

    def get_serializer_class(self):
        if self.action == "create_offer":
            return OfferCreateSerializer
        elif self.action == "add_to_watchlist":
            return WatchListSerializer
        else:
            return ItemSerializer

    @action(methods=['POST'], detail=True)
    def add_to_watchlist(self, request, pk=None):
        item = Item.objects.filter(pk=pk).first()
        watch_list = Watchlist.objects.get(user=self.request.user)
        watch_item = WatchlistItem.objects.create(item=item, user=self.request.user)
        watch_list.watchlist_items.add(watch_item)
        if watch_list.watchlist_items.filter(user=self.request.user, id=item.id).exists():
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'], detail=True)
    def create_offer(self, request, pk=None):
        item = Item.objects.filter(pk=pk).first()
        user = request.user
        serializer = self.get_serializer(data=request.data, context={
            "request": request,
            "item": item,
        })
        if serializer.is_valid():
            serializer.save(user=user, item=item)
            return response.Response(serializer.data,
                                     status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors,
                                 status=status.HTTP_400_BAD_REQUEST)
