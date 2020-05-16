from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """Test API view"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """List the API features"""
        an_apiview = [
            "Uses HTTP methods and functions (get, post, update, put, delete)",
            "Is similar to a traditional Django View",
            "Gives you the most control over application logic",
            "Is mapped manually to URLs",
        ]

        return Response({"message": "hello", "an_apiview": an_apiview})

    def post(self, request):
        """create a hello Message with name"""
        serializer = self.serializer_class(data=request.data)
        # return Response({"extra": "succes"})

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello, the name is {name}"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """handle updating an object"""
        return Response({"methode": "PUT"})

    def patch(self, request, pk=None):
        """handle a partial update of an object"""
        return Response({"methode": "PATCH"})

    def delete(self, request, pk=None):
        """handle the delete of an object"""
        return Response({"methode": "DELETE"})
