from django.urls import include, path

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

app_name = "trade"
urlpatterns = [
              ] + router.urls
