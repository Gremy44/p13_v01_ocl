from django.shortcuts import render
from .models import Letting
from oc_lettings_site.logger import capture_sentry_message


@capture_sentry_message
def index(request):
    """
    Renders the lettings index page.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Rendered HTML response for the lettings index page displaying a list of lettings.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


@capture_sentry_message
def letting(request, letting_id):
    """
    Renders the details page for a specific letting.

    Parameters:
    - request: The HTTP request object.
    - letting_id: The ID of the letting to be displayed.

    Returns:
    - Rendered HTML response for the letting details page.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
