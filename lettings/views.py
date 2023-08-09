from django.shortcuts import render
from .models import Letting


def index(request):
    """
    Renders the index page.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Rendered HTML response for the index page.
    """
    return render(request, "index.html")


def lettings_index(request):
    """
    Renders the lettings index page.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Rendered HTML response for the lettings index page displaying a list of lettings.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings_index.html", context)


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
    return render(request, "letting.html", context)
