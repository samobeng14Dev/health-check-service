from django.utils.timezone import now
from django.template.response import TemplateResponse
from django.urls import path

from health_check.services import check_endpoint_health

from .models import Endpoint, HealthCheckResult
from django.contrib import admin

from health_check.models import Endpoint, HealthCheckResult



@admin.register(Endpoint)
class EndpointAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at', 'updated_at')
    actions = ['run_health_check']  
    search_fields = ('name', 'url')
    ordering = ('name',)

    def run_health_check(self, request, queryset):
        for endpoint in queryset:
            check_endpoint_health(endpoint)
        self.message_user(
            request, "Health checks triggered for selected endpoints.")
    run_health_check.short_description = "Run health check for selected endpoints"



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



