from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


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


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Return a hello message"""

        a_viewset = [
            "Uses action (list, create, retrieve, update, partial_update)",
            "Automatically maps to URLs using Routers",
            "Provides more functionality with less code",
        ]

        return Response({"message": "Hello!", "a_viewset": a_viewset})

    def create(self, request):
        """ create a new hello message """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """ Handle getting an object by its ID """
        return Response({"http_messsage": "GET"})

    def update(self, request, pk=None):
        """ Handle updating an object """
        return Response({"http_message": "PUT"})

    def partial_update(self, request, pk=None):
        """ Handle a partial update """
        return Response({"http_message": "PATCH"})

    def destroy(self, request, pk=None):
        """ Handle a delete """
        return Response({"http_message": "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objectss.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        "name",
        "email",
    )


class UserLoginApiView(ObtainAuthToken):
    """ Handle creating user authentication tokens """

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ Handles creating, reading and updating profile feed items"""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permissions_classes = (permissions.UpdateOwnStatus, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        """Set the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
