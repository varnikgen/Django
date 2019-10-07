from django.urls import path
from portalapp.views import example_view

urlpatterns = [
    path('', example_view)
]