from rest_framework.permissions import BasePermission

from apps.core.constants import HttpMethodsCts as cts


class IsObjectOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return (
            request.method in cts.SAFE or
            request.user.is_staff or
            obj.owner.user == request.user
        )


class IsStafforListIsForbidden(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_staff or not view.action == 'list'
