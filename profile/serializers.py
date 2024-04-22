from rest_framework import serializers

from core.api.serializers import BaseUIDSerializer, BirthdateSerializer
from profile.models import Profile


class SocialLinkSerializer(BaseUIDSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'link_type', 'url')
        read_only_fields = ('id',)


class ProfileSerializer(BaseUIDSerializer):
    user_id = serializers.UUIDField(source='user.uid', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    phone_number = serializers.CharField(source='user.phone', read_only=True)
    birth_date = BirthdateSerializer(required=True, minimum_age=13, allow_future_date=False)
    social_links = SocialLinkSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = (
            'id', 'user_id', 'first_name', 'last_name', 'email', 'phone_number', 'bio', 'location', 'birth_date',
            'image', 'social_links')
        read_only_fields = ('id', 'user')
