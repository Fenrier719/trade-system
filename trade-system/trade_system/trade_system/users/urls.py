from django.urls import path
from rest_framework.routers import DefaultRouter

from trade_system.users.api.views import (
    UserViewSet
)

router = DefaultRouter()
router.register("", UserViewSet)
app_name = "users"
urlpatterns = router.urls
