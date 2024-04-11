from rest_framework import serializers
from .models import EventsModel

class EventsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventsModel
        fields = ('title', 'description')


