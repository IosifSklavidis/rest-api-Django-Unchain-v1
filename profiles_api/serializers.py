from rest_framework import serializers

from profiles_api import models

class HelloSerializer(serializers.Serializer):
    # Serializer a name field for testing our APIView
    # similar to Django Forms
    # take care of validation rules
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    # serializers a user profile object
    # when we create our password field for our model set it to write only
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    # override the create with a new one
    def create(self, validated_data):
    # create and return a new user
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    # serializes profile feed item

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
