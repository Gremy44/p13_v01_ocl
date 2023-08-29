from django.urls import path
from .views import index as index, letting

urlpatterns = [
    path('', index, name='lettings_index'),
    path('<int:letting_id>/', letting, name='letting'),
]
