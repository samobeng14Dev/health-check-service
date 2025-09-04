from django.db import models

# Create your models here.
class Endpoint(models.Model):
    name=models.CharField(max_length=100)
    url=models.URLField()
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['name']

    def __str__(self):
        return f'{self.name} - {self.url}'

class HealthCheckResult(models.Model):
    endpoint=models.ForeignKey(Endpoint, on_delete=models.CASCADE)
    status_code=models.IntegerField(null=True, blank=True)
    response_time=models.FloatField(help_text="Response time in seconds")
    is_up=models.BooleanField(default=False)
    error_message=models.TextField(null=True, blank=True)
    checked_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-checked_at']

    def __str__(self):
        status="UP" if self.is_up else "DOWN"
        return f'{self.endpoint.name} - {status} at {self.checked_at}'    