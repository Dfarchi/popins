import os
from requests import request

from rest_framework import status, permissions, mixins, viewsets
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..models import Profile, User
from ..serializers.ProfileSerializer import ProfileEmailSerializer, ProfileSerializer
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login


# from google.auth.transport import requests
# from google.oauth2 import id_token


class ProfileView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [permissions.AllowAny, permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_serializer(self, *args, **kwargs):
        if self.request.method == "PATCH":
            return ProfileEmailSerializer(args[0], **kwargs)
        return ProfileSerializer(args[0], **kwargs)
        # return super().get_serializer(*args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        user_id = kwargs.get("pk") if "pk" in kwargs else self.request.user.id
        return Profile.objects.get(user_id=user_id)

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            instance = self.get_queryset(*args, **kwargs)
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_queryset(request, *args, **kwargs)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.data)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
