# BruteBuster by Cyber Security Consulting (www.csc.bg)

"""
Brutebuster needs access to the REMOTE_IP of the incoming request. We're doing
this by adding the request object to the thread_local space
"""

try:
    from threading import local
except ImportError:
    from django.utils.threading_local import local

_thread_locals = local()


def get_request():
    return getattr(_thread_locals, 'request', None)


class RequestMiddleware(object):
    """Provides access to the request object via thread locals"""

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        _thread_locals.request = request
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response