from rest_framework import mixins, permissions, viewsets

from apps.core.permissions import IsObjectOwner, IsStafforListIsForbidden
from apps.events.choices import EventStateChoices, MembershipStateChoices
from apps.events.exceptions import EventIsFullAPIException
from apps.events.models import Event, Membership
from apps.events.serializers import EventSerializer, MembershipSerializer


class EventModelViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Event.objects.order_by('-created_at').filter(
        state=EventStateChoices.ACTIVE
    )
    serializer_class = EventSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsObjectOwner,
        IsStafforListIsForbidden
    )


class MembershipModelViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Membership.objects.order_by('-created_at').filter(
        state=MembershipStateChoices.PAID
    )
    serializer_class = MembershipSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsObjectOwner,
        IsStafforListIsForbidden
    )

    def perform_create(self, serializer):
        event = serializer.validated_data.get('event')
        if event.is_full():
            raise EventIsFullAPIException()
        super(MembershipModelViewSet, self).perform_create(serializer=serializer)
