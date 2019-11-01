from rest_framework.routers import DefaultRouter

from .views import (
    EventModelViewSet,
    MembershipModelViewSet,
)

app_name = 'events'

router = DefaultRouter()
router.register(r'event', EventModelViewSet, basename='events')
router.register(r'membership', MembershipModelViewSet, basename='memberships')

urlpatterns = router.urls
