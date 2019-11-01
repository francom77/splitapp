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

    def validate(self, data):
        event = data.get('event')
        membership_count = event.memberships.filter(
            state=MembershipStateChoices.PAID
        ).count()
        if event.max_memberships is not None and membership_count >= event.max_memberships:
            raise serializers.ValidationError("Max number of members reached")
        return data


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
