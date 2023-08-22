from django.contrib import admin
from django.urls import path, include

from .views import index, trigger_error

urlpatterns = [
    path('', index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('error500/', trigger_error),
    path('admin/', admin.site.urls),
]

handler404 = 'oc_lettings_site.views.error_404_view'
handler500 = 'oc_lettings_site.views.error_500_view'
