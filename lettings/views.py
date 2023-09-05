from django.shortcuts import render
from .models import Letting
from oc_lettings_site.logger import capture_sentry_message


@capture_sentry_message
def index(request):
    """
    Render the lettings index page.

    This view function renders the index page for lettings,
    displaying a list of all available lettings.

    :param request: The HTTP request object.
    :type request: HttpRequest

    :return: Rendered HTML response for the lettings index page displaying a list of lettings.
    :rtype: HttpResponse
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


@capture_sentry_message
def letting(request, letting_id):
    """
    Render the details page for a specific letting.

    This view function renders the details page for a specific letting, identified by its ID.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :param letting_id: The ID of the letting to be displayed.
    :type letting_id: int

    :return: Rendered HTML response for the letting details page.
    :rtype: HttpResponse
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
