from django.contrib.auth.models import User
from rest_framework import serializers
from ..models import Session


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.date = validated_data.get("date", instance.date)
        instance.salary = validated_data.get("salary", instance.salary)
        instance.note = validated_data.get("note", instance.note)
        instance.has_happened = validated_data.get(
            "has_happened", instance.has_happened
        )

        instance.save()
        return instance
