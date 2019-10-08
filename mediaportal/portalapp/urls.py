from django.urls import path
from portalapp.views import BaseView

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
]
