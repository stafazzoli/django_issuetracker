from rest_framework import permissions
from projects.models import Issue


class IsReporter(permissions.BasePermission):
    """Custom permission class to allow only issue reported to delete/ update them."""
    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the issue owner."""
        # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.reporter == request.user
