from rest_framework import permissions, viewsets

from apps.wallet.models import Movement
from apps.wallet.serializers import MovementSerializer


class MovementModelViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = MovementSerializer

    def get_queryset(self):
        return Movement.objects.filter(owner_id=self.request.user.userprofile.id)
