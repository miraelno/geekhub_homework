from django.contrib import messages
from django.shortcuts import redirect

class AuthenticatedMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.add_message(request, messages.ERROR, "You don't have access to this page.")
            return redirect('templates:product_list')
        return super(AuthenticatedMixin, self).dispatch(request, *args, **kwargs)
