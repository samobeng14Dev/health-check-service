from rest_framework import serializers
from health_check.models import HealthCheckResult, Endpoint

class EndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endpoint
        fields = '__all__'

class HealthCheckResultSerializer(serializers.ModelSerializer):
    endpoint = EndpointSerializer(read_only=True)

    class Meta:
        model = HealthCheckResult
        fields = '__all__'