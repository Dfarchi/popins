from rest_framework import generics, status, permissions, mixins, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..serializers.InterestSerializer import InterestSerializer
from ..models import Interest


class Interest_view(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
):
    permissions_classes = [permissions.AllowAny, permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = InterestSerializer
    queryset = Interest.objects.all()

    # Might be unnecessary
    def get_queryset(self, *args, **kwargs):
        user_id = kwargs.get.pk("pk")
        return Interest.objects.get(user_id=user_id)

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().retrieve(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, *args, **kwargs):
        # understand this one :
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
