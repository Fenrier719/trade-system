from django.contrib.auth import get_user_model
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import  InventoryListSerializer
from ..models import InventoryItem

User = get_user_model()


class InventoryViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = InventoryListSerializer
    queryset = InventoryItem.objects.all()

    def get_queryset(self):
        return InventoryItem.objects.select_related('user') \
            .select_related("item") \
            .filter(user=self.request.user)
