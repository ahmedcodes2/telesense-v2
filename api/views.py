from functools import wraps

from django.db.models.expressions import result
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Telemetry
from api.serializers import TelemetrySerializer


def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"finished {func.__name__}")
        return result
    return wrapper

@log_execution
@api_view(['GET'])
def hello(request):
    return Response({'message': 'Hello World!'})

print(hello.__name__)

class TelemetryCreateView(generics.CreateAPIView):
    queryset = Telemetry.objects.all()
    serializer_class = TelemetrySerializer




