from rest_framework.routers import DefaultRouter

from .views import (
    MovementModelViewSet
)

app_name = 'wallet'

router = DefaultRouter()
router.register(r'movement', MovementModelViewSet, basename='movements')

urlpatterns = router.urls
