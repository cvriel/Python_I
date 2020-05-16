from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Seralizes a name field for testing the APIView"""

    name = serializers.CharField(max_length=10)
