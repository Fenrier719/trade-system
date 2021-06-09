from django.contrib.auth import get_user_model
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from trade_system.watchlists.api.serializers import WatchlistItemSerialize
from trade_system.watchlists.models import WatchlistItem

User = get_user_model()


class WatchListViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = WatchlistItemSerialize
    queryset = WatchlistItem.objects.all()

    def get_queryset(self):
        return WatchlistItem.objects.select_related('user') \
            .select_related("item") \
            .filter(user=self.request.user)
