from django.contrib.auth import get_user_model
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from ..models import Offer

from .serializers import OfferListSerializer

User = get_user_model()


class OfferViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = OfferListSerializer
    queryset = Offer.objects.all()

