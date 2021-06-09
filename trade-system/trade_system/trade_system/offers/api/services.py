from django.contrib.auth import get_user_model
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from trade_system.offers.api.serializers import OfferListSerializer
from trade_system.offers.models import Offer

User = get_user_model()


class OfferViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = OfferListSerializer
    queryset = Offer.objects.all()
