from django.shortcuts import render, HttpResponse
from sentry_sdk import capture_message
from datetime import datetime


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
    
    # capture_message(f"Error 404 for {request.user} at {datetime.now()}", level="error")
    
    return render(request, "errors/404/404.html", status=404)


def error_500_view(request, exception=None):
    """
    Renders the custom 500 page, error server.

    Parameters:
    - request: The HTTP request object.
    - exception: The exception that triggered the 500 error.

    Returns:
    - Rendered HTML response for the custom 500 page.
    """
    return render(request, "errors/500/500.html", status=500)


from django.http import HttpResponse

def error_view(request):
    try:
        # Simuler une erreur interne en levant une exception.
        raise Exception("Simulated Internal Server Error")
    except Exception as e:
        # Si une exception est générée, renvoyer une réponse avec le code de statut 500.
        return HttpResponse("Internal Server Error", status=500)
    return HttpResponse("This view should not be reached.")
