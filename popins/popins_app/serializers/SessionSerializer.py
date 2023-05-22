from django.contrib.auth.models import User
from rest_framework import serializers
from ..models import Session


class SessionSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source="user.username")
    # date = serializers.DateField()
    # # salary = serializers.IntegerField()
    # note = serializers.CharField()
    # # has_happened = serializers.BooleanField()
    # # interested_nannies = serializers.ReadOnlyField(
    # #     source="user.Interest", related_name="sessions"
    # # )

    # username = serializers.SerializerMethodField()

    # def get_username(self, obj):
    #     return obj.user.username

    class Meta:
        model = Session
        fields = "__all__"

    # class SessionUserSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = User
    #         fields = [
    #             "username",
    #         ]

    def update(self, instance, validated_data):
        instance.date = validated_data.get("date", instance.date)
        instance.salary = validated_data.get("salary", instance.salary)
        instance.note = validated_data.get("note", instance.note)
        instance.has_happened = validated_data.get(
            "has_happened", instance.has_happened
        )

        instance.save()
        return instance
