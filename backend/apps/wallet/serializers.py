from rest_framework import serializers

from apps.wallet.models import Movement


class MovementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movement
        fields = [
            'id', 'amount', 'description',
        ]
