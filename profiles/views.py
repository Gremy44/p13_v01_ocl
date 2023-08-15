from django.shortcuts import render
from .models import Profile


def index(request):
    """
    Renders the profiles index page.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Rendered HTML response for the profiles index page displaying a list of profiles.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Renders the details page for a specific user's profile.

    Parameters:
    - request: The HTTP request object.
    - username: The username of the profile to be displayed.

    Returns:
    - Rendered HTML response for the profile details page.
    """
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
