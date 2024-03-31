from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event
import logging
import json
from django.core.serializers import serialize

logger = logging.getLogger(__name__)

class EventAPIView(APIView):
    def post(self, request, *args, **kwargs):
        event_data = request.data
        event = Event.objects.create(
            type=event_data.get('type'),
            path=event_data.get('path'),
            details=event_data
        )
        logger.info(f"Event received: {event}")
        return Response({"status": "success"}, status=201)


def event_statistics(request):
    # Retrieve all event records from the database
    events = Event.objects.all()
    # You can perform aggregation or data processing here if needed
   
    return render(request, 'statistics.html', {'events': events})
# def event_statistics(request):
#     events = Event.objects.all()
#     # Serialize the queryset to JSON string
#     events_json = serialize('json', events)
#     # Send events as a JSON response to be used by JavaScript
#     return render(request, 'statistics.html', {'events': events_json})

