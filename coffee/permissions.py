from rest_framework import permissions


class IsUserOrIsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user and request.user.is_authenticated and request.user.role=='admin':
            return True
        return False
