from django.contrib.auth import authenticate
from django.utils.translation import gettext as _
from rest_framework import serializers

from authentication.models import User
from core.api.serializers import BaseUIDSerializer, BirthdateSerializer


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    remember_me = serializers.BooleanField(write_only=True, default=False)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                data['user'] = user
                data['token'] = user.get_token()
            else:
                raise serializers.ValidationError(_('Unable to login with provided credentials'))
        else:
            raise serializers.ValidationError(_('Must include "email" and "password"'))

        return data


class UserSerializer(BaseUIDSerializer):
    password = serializers.CharField(write_only=True)
    # token = serializers.SerializerMethodField()
    birth_date = BirthdateSerializer(read_only=True, source='profile.birth_date')
    image = serializers.ImageField(read_only=True, source='profile.image')
    bio = serializers.CharField(read_only=True, source='profile.bio')
    location = serializers.CharField(read_only=True, source='profile.location')
    # social_links = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'password', 'birth_date', 'image', 'bio',
                  'location']

    @staticmethod
    def get_token(obj):
        return obj.get_token()
