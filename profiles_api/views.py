# start

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# status -> i can use for having responses from an API

from profiles_api import serializers

class HelloApiView(APIView):
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
            
