from django.shortcuts import redirect
from django.contrib import messages

def validate_session(view_func):
    """Decorator to validate session data."""
    def _wrapped_view(request, *args, **kwargs):
        if 'my_key' not in request.session:
            messages.error(request, "Your session has expired. Please log in again.")
            return redirect('login_view')  # Redirect to login if session data is not found
        return view_func(request, *args, **kwargs)
    return _wrapped_view

