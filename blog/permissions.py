from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAVE_METHODS:
            return True
        return obj.user == request.user or request.user.is_superuser