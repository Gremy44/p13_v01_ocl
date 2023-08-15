import logging
from django.contrib import admin
from datetime import datetime

logger = logging.getLogger("admin_logger")


class MyAdminSite(admin.AdminSite):
    def each_context(self, request):
        logger.info(f"User '{request.user}' logged in to the admin site at {datetime.now()}")
        return super().each_context(request)


admin_site = MyAdminSite(name="myadmin")
