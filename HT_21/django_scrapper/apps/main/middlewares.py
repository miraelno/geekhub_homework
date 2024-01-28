from django.utils.deprecation import MiddlewareMixin
from django.contrib import messages
from django.shortcuts import redirect


class CustomPermissionIsSuperUserMiddleware(MiddlewareMixin):
    not_allowed_endpoints = {'/product/add/': ['GET', 'POST'], }
    
    def process_request(self, request):
        for endpoint, methods in self.not_allowed_endpoints.items():
            if request.path.startswith(endpoint) and request.method in methods:
                if not bool(request.user and request.user.is_staff and request.user.is_superuser):
                    messages.add_message(request, messages.ERROR, "You have no permissions for this action.")
                    return redirect("main:product_list")
