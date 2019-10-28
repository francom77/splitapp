from rest_framework import permissions, viewsets

from apps.core.permissions import IsObjectOwner, IsStafforListIsForbidden
from apps.events.choices import EventStateChoices
from apps.events.models import Event
from apps.events.serializers import EventSerializer


class EventModelViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.order_by('-created_at').filter(
        state=EventStateChoices.ACTIVE
    )
    serializer_class = EventSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsObjectOwner,
        IsStafforListIsForbidden
    )
