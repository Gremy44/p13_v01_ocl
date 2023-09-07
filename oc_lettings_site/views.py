from django.shortcuts import render, HttpResponse
from .logger import capture_sentry_message
from sentry_sdk import capture_message
from datetime import datetime


@capture_sentry_message
def index(request):
    """
    Renders the index page.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Rendered HTML response for the index page.
    """
    return render(request, "index.html")


def error_404_view(request, exception=None):
    """
    Renders the custom 404 page, page not found.

    Parameters:
    - request: The HTTP request object.
    - exception: The exception that triggered the 404 error.

    Returns:
    - Rendered HTML response for the custom 404 page.
    """
    ip_user = request.META.get('REMOTE_ADDR')
    capture_message(f"Error 404 for {ip_user} at {datetime.now()}", level="warning")
    return render(request, "errors/404.html", status=404)


def error_500_view(request, exception=None):
    """
    Renders the custom 500 page, error server.

    Parameters:
    - request: The HTTP request object.
    - exception: The exception that triggered the 500 error.

    Returns:
    - Rendered HTML response for the custom 500 page.
    """
    ip_user = request.META.get('REMOTE_ADDR')
    capture_message(f"Error 500 for {ip_user} at {datetime.now()}", level="error")
    return render(request, "errors/500.html", status=500)


def error_view(request):
    """
    This view simulates an internal server error by raising
    an exception and returns an appropriate response.

    Args:
        request (HttpRequest): The incoming HTTP request object.

    Returns:
        HttpResponse: A response indicating an internal server error with a status code of 500.
    """
    return HttpResponse('Simulate internal server error', status=500)
