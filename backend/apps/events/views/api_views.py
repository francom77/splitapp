from rest_framework import permissions, viewsets

from apps.core.permissions import IsObjectOwner, IsStafforListIsForbidden
from apps.events.choices import EventStateChoices, MembershipStateChoices
from apps.events.models import Event, Membership
from apps.events.serializers import EventSerializer, MembershipSerializer


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


class MembershipModelViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.order_by('-created_at').filter(
        state=MembershipStateChoices.PAID
    )
    serializer_class = MembershipSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsObjectOwner,
        IsStafforListIsForbidden
    )
