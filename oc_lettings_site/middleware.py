from django.shortcuts import render


class CustomErrorMiddleware:
    def __init__(self, get_response):
        """
        Custom middleware for rendering custom error pages.

        Parameters:
        - get_response: The callable that represents the next middleware or view.

        Returns:
        - None
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Process the request and render custom error pages if applicable.

        Parameters:
        - request: The HTTP request object.

        Returns:
        - Rendered HTML response for custom error pages or the
        response from the next middleware/view.
        """
        response = self.get_response(request)
        if response.status_code == 404:
            return render(request, "404/404.html", status=404)
        elif response.status_code == 405:
            return render(request, "405/405.html", status=405)
        return response
