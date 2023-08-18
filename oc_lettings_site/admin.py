from django.contrib.auth.signals import user_logged_in
from sentry_sdk import capture_message


def capture_admin_login(sender, request, user, **kwargs):
    """
    Capture admin login event.

    This function is connected to the `user_logged_in` signal to capture when an admin user
    logs in to the administration interface. It logs an informational message with details
    about the logged-in user, such as their username, and attaches relevant tags.

    Args:
        sender: The sender of the signal.
        request: The request object associated with the login event.
        user: The user who logged in.
        **kwargs: Additional keyword arguments provided by the signal.

    Returns:
        None
    """
    capture_message(
        f"User {user.username} logged in to the admin interface",
        level="info",
        tags={"user_logged": user.username},
    )


# Connect the signal to the function
user_logged_in.connect(capture_admin_login)
