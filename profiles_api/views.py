from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """List the API features"""
        an_apiview = [
            "Uses HTTP methods and functions (get, post, update, put, delete)",
            "Is similar to a traditional Django View",
            "Gives you the most control over application logic",
            "Is mapped manually to URLs",
        ]

        return Response({"message": "hello", "an_apiview": an_apiview})
