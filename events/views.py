from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Event
from .serializers import EventSerializer


@api_view(['GET'])
def event_list(request):
    
    events = Event.objects.filter(
        is_published=True
    )
    
    serializer = EventSerializer(
        events,
        many=True
    )
    
    return Response(serializer.data)

