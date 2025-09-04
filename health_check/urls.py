from django.contrib import admin
from django.urls import path, include
from health_check.views import HealthCheckListAPIView

urlpatterns = [
    path('health/', HealthCheckListAPIView.as_view(), name='health-check'),
]
