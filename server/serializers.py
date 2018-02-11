from django.contrib.auth.models import User

from rest_framework import serializers

from .models import GoogleUser

''' Script Used to convert python objects to json objects.'''


class UserSerializer(serializers.ModelSerializer):
    """User Model serializer class."""

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class GoogleUserSerializer(serializers.ModelSerializer):
    """GoogleUser Model serializer class."""

    class Meta:
        model = GoogleUser
        fields = ('google_id', 'app_user', 'appuser_picture', 'slack_name')
        depth = 1


class CustomUserSerializer(serializers.ModelSerializer):
    """Custom User Model serializer class."""

    class Meta:
        model = GoogleUser
        fields = ('slack_name', 'app_user')
        depth = 1