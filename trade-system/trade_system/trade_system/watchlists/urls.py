from rest_framework.routers import DefaultRouter

from trade_system.watchlists.api.services import (
    WatchListViewSet,
)

router = DefaultRouter()
router.register(r'watchlist', WatchListViewSet)
app_name = "watchlists"
urlpatterns = router.urls
