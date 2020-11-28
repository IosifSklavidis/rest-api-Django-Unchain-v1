# start

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
# status -> i can use for having responses from an API

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

# APIView
class HelloApiView(APIView):
    # Apiview is for HTTP functions
    # Test API View
    # whener u send a post, put or patch request expect an input with name
    # and validated with max length of 10 as the serializers.property
    serializers_class = serializers.HelloSerializer

    def get(self, request, format=None):
        # Returns a list of APIView features
        an_apiview = [
            'Uses HTTP methods as function(get, post, patch, put, delete)'
            'Is similar to a traditional Django View'
            'Gives you the most control over your app Logic'
            'Is mapped manually to URLS'
        ]

        # dictionary {}
        return Response({'message': 'Hello', 'an_apiview': an_apiview})


        def post(self, request):
            # Create a hello message with our name
            serializer = self.serializers_class(data=request.data)
            # the data is assigned to our serializer class

            if serializer.is_valid():
                name = serializer.validated_data.get('name')
                message = f'Hello {name}'
                return Response({'message': message})
            else:
                return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        def put(self, request, format=None):
            # Update an object
            return Response({'method':'PUT'})

        def patch(self, request, pk=None):
            # Handle a partial update of an object
            return Response({'method':'PATCH'})

        def delete(self, request, pk=NONE):
            return Response({'method':'DELETE'})

# Viewset
class HelloViewSet(viewsets.Viewset):
    # API VIEWSET
    serializers_class = serializers.HelloSerializer

    def list(self, request):
        # Return a hello message
        # it will create this list below and it will return as response in our API
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        # Create a new hello message
        # retrieve using the serializer class
        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    # i pass a pk to retrieve it through pk
    def retrieve(self, request, pk=None):
    # get an object through id
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})


class UserProfileViewset(viewsets.ModelViewset):
    # handle creating and updating profiles
    serializers_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    # how the user has permissions
    permission_classes = (permissions.UpdateOwnProfile,)
    # add search filtering
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):
    # create user authentication tokens
    # it adds renderer_classes to ObtainAuthToken
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileViewset(viewsets.ModelViewset):
    # handles creating, reading, updating profile feed items
    authentication_classes = (TokenAuthentication,)
    serializers_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        # sets the user profile to the logged in user
        serializer.save(user_profile=self.request.user)
