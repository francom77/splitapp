from rest_framework.routers import DefaultRouter

from .views import (
    EventModelViewSet,
)

app_name = 'events'

router = DefaultRouter()
router.register(r'events', EventModelViewSet, basename='events')

urlpatterns = router.urls
