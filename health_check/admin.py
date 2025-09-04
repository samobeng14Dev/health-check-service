from django.utils.timezone import now
from django.template.response import TemplateResponse
from django.urls import path

from .models import Endpoint, HealthCheckResult
from django.contrib import admin

from health_check.models import Endpoint, HealthCheckResult

# Register your models here.


@admin.register(Endpoint)
class EndpointAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'url')
    ordering = ('name',)


@admin.register(HealthCheckResult)
class HealthCheckResultAdmin(admin.ModelAdmin):
    list_display = (
        'endpoint', 'status_code', 'response_time', 'is_up', 'checked_at', 'error_message'
    )
    list_filter = ('is_up', 'status_code', 'checked_at')
    search_fields = ('endpoint__name', 'error_message')
    readonly_fields = ('endpoint', 'status_code', 'response_time',
                       'is_up', 'checked_at', 'error_message')
    ordering = ('-checked_at',)



