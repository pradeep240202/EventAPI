from rest_framework.permissions import BasePermission

# Only admin users are allowed to create events
class EventPermisison(BasePermission):
    message = "Only admin users are allowed to create events"

    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        if request.user.role == "Admin" and request.method == "POST":
            return True
        
        return False