from rest_framework.routers import DefaultRouter

from trade_system.items.api.services import (
    ItemListViewSet,
)

router = DefaultRouter()

router.register(r'items', ItemListViewSet)
app_name = "items"
urlpatterns = router.urls
