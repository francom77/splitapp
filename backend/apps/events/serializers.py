from rest_framework import serializers

from core.fields import CurrentProfileDefault
from apps.events.choices import MembershipStateChoices
from apps.events.models import Event, Membership


class MembershipSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=CurrentProfileDefault())

    class Meta:
        model = Membership
        fields = ['id', 'event', 'owner']


class EventSerializer(serializers.ModelSerializer):

    members_queryset = Membership.objects.order_by('-created_at').filter(
        state=MembershipStateChoices.PAID
    )

    memberships = MembershipSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = [
            'id', 'date_time', 'name', 'max_memberships', 'suscription_amount',
            'owner', 'memberships'
        ]
