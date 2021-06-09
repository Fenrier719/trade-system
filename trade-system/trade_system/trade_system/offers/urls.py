from rest_framework.routers import DefaultRouter

from trade_system.offers.api.services import (
    OfferViewSet,
)

router = DefaultRouter()
router.register(r'offers', OfferViewSet)
app_name = "offers"
urlpatterns = router.urls
