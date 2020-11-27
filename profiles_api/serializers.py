from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    # Serializer a name field for testing our APIView
    # similar to Django Forms
    # take care of validation rules
    name = serializers.Charfield(max_length=10)
