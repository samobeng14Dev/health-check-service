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
    list_display = ('endpoint', 'status_code', 'is_up',
                    'response_time', 'checked_at')
    list_filter = ('is_up', 'checked_at')
    search_fields = ('endpoint__name', 'endpoint__url', 'error_message')
    ordering = ('-checked_at',)
