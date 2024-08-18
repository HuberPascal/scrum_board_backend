# scrumboardbackend/middleware.py

from django.conf import settings
from django.contrib.auth import logout
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

class SessionTimeoutMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.user.is_authenticated:
            return

        current_time = timezone.now()
        session_expiry_time = request.session.get('last_activity') or current_time
        elapsed_time = (current_time - session_expiry_time).total_seconds()

        if elapsed_time > settings.SESSION_COOKIE_AGE:
            logout(request)
        else:
            request.session['last_activity'] = current_time
