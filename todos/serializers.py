from .models import Todo
from rest_framework import serializers

## Create a Serializer for Our Model
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    # nest a Meta class to configure the serializer
    class Meta:
        # which model does it serialize
        model = Todo
        # which fields should be serialized
        fields = ["id", "subject", "details"]