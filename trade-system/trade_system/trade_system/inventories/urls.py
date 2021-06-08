from rest_framework.routers import DefaultRouter

from trade_system.inventories.api.services import (
    InventoryViewSet,
)

router = DefaultRouter()
router.register(r'inventory', InventoryViewSet)
app_name = "inventories"
urlpatterns = router.urls
