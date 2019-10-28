from rest_framework import serializers

from apps.events.models import Event


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'id', 'date_time', 'name', 'max_memberships', 'suscription_amount',
            'owner'
        ]
