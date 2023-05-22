from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()

    def get_email(self, obj):
        return obj.user.email

    class Meta:
        model = Profile
        fields = "__all__"


class ProfileEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
        ]


    def update(self, instance, validated_data):
        # Might work too, didn't try:
        # instance.user.email = validated_data["email"]
        # instance.user.save()
        setattr(instance.user, "email", validated_data["email"])
        instance.user.save()
        instance.save()
        return instance.user
