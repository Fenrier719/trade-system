from celery import shared_task
from django.contrib.auth import get_user_model
from trade_system.offers.models import Offer

User = get_user_model()


@shared_task
def delete_inactive_offers():
    Offer.objects.filter(is_active=False).delete()


delete_inactive_offers.delay()
