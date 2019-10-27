from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response


class FiniteStateMachineViewSetMixin(object):

    @action(detail=True, methods=['patch', ], name="Change State")
    def change_state(self, request, pk):
        next_state = request.data.get('next_state')
        obj = self.get_object()
        obj.change_state(next_state, user=request.user)

        return Response(status=status.HTTP_200_OK, data=self.serializer_class(obj).data)
