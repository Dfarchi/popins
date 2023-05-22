from rest_framework import serializers
from django.contrib.auth.models import User

from ..models import Profile


class UserSerializer(serializers.ModelSerializer):
    profile_pic = serializers.SerializerMethodField()

    def get_profile_pic(self, obj):
        return obj.user_profile.profile_pic

    def get_liked_apartments(self, obj):
        return obj.liked_apartments

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "is_parent",
            "profile_pic",
            "bio",
            "birth_year",
            "address",
            "link",
        ]