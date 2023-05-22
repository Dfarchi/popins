from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response


class LogoutView(APIView):
    def post(self, request):
        refresh_token = request.data.get("refresh_token")

        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response({"detail": "Successfully logged out."})
            except:
                return Response({"detail": "Invalid refresh token."}, status=400)
        else:
            return Response({"detail": "Refresh token is required."}, status=400)
