import requests
import time
from django.utils import timezone
from health_check.models import Endpoint, HealthCheckResult

def check_endpoint_health(endpoint):
    '''Check the health of a single endpoint.'''
    start_time=time.time()
    try:
        response=requests.get(endpoint.url, timeout=5,headers={'User-Agent': 'HealthCheckService/1.0'})
        response_time=time.time()-start_time
        is_up=response.status_code==200

        return HealthCheckResult(
            endpoint=endpoint,
            status_code=response.status_code,
            response_time=response_time,
            is_up=is_up,
            error_message=None if is_up else f'Unexpected status code: {response.status_code}',
            checked_at=timezone.now()

        )
    except requests.RequestException as e:
        response_time=time.time()-start_time
        return HealthCheckResult(
            endpoint=endpoint,
            status_code=None,
            response_time=response_time,
            is_up=False,
            error_message=str(e),
            checked_at=timezone.now()
        )

def check_all_active_endpoints():
    '''Check the health of all active endpoints.'''
    endpoints=Endpoint.objects.filter(is_active=True)
    results=[]
    for endpoint in endpoints:
        result=check_endpoint_health(endpoint)
        result.save()
        results.append(result)
    return results



