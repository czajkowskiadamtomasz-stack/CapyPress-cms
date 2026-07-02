from django.http import HttpResponse
from .selectors import get_site_settings


class MaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        settings = get_site_settings()

        if settings.maintenance_mode and not request.user.is_staff:
            return HttpResponse("Maintenance mode", status=503)

        return self.get_response(request)
