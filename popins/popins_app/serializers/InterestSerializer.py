from rest_framework import serializers
# from django.contrib.auth.models import
from models import Interest


class InterestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interest
        fields = "__all__"