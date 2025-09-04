from rest_framework import generics, status
from rest_framework.response import Response
from .models import HealthCheckResult, Endpoint
from .serializers import HealthCheckResultSerializer
from .services import check_all_active_endpoints



class HealthCheckListAPIView(generics.ListAPIView):
   '''API view to list all health check results.'''
   serializer_class=HealthCheckResultSerializer

   def get_queryset(self):
      latest_results=[]
      for endpoint in Endpoint.objects.filter(is_active=True):
         latest=HealthCheckResult.objects.filter(endpoint=endpoint).order_by('-checked_at').first()
         if latest:
            latest_results.append(latest.id)
      
      return HealthCheckResult.objects.filter(id__in=latest_results).order_by('-checked_at')
   
   def list (self, request, *args, **kwargs):
      if request.query_params.get('check_now')=='true':
         check_all_active_endpoints()

      response=super().list(request, *args, **kwargs)
      '''Add summary statistics to the response.'''
      endpoints=Endpoint.objects.filter(is_active=True)
      up_count=sum(1 for endpoint in endpoints if HealthCheckResult.objects.filter(endpoint=endpoint, is_up=True).order_by('-checked_at').first())

      summary={
         'total_endpoints': endpoints.count(),
         'up_endpoints': up_count,
         'down_endpoints': endpoints.count()-up_count,
         'timestamp': self.get_queryset().first().checked_at if self.get_queryset() else None
      }

      response.data={'summary': summary, 'results': response.data}
      return response
        
