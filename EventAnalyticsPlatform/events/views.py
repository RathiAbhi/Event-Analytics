from rest_framework import viewsets
from .serializers import EventsSerializer
from .models import EventsModel

class EventsViewSet(viewsets.ModelViewSet):
    queryset = EventsModel.objects.all()
    serializer_class = EventsSerializer
