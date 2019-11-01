from rest_framework import serializers

from apps.core.fields import CurrentProfileDefault
from apps.events.choices import MembershipStateChoices
from apps.events.models import Event, Membership


class MembershipSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=CurrentProfileDefault())
    state_display = serializers.CharField(source='get_state_display', read_only=True)

    class Meta:
        model = Membership
        fields = ['id', 'event', 'owner', 'state_display']


class EventSerializer(serializers.ModelSerializer):

    memberships = MembershipSerializer(many=True, read_only=True)
    is_full = serializers.BooleanField(read_only=True)

    class Meta:
        model = Event
        fields = [
            'id', 'date_time', 'name', 'max_memberships', 'suscription_amount',
            'owner', 'memberships', 'is_full'
        ]
