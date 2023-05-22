from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views.Session_viewset import SessionViewSet

from .views.Register_viewset import RegistrationView
from .views.Profile_viewset import ProfileView, google_oauth

urlpatterns = [
    path("auth/google-oauth/", google_oauth, name="google-oauth"),
    path(
        "profile/",
        ProfileView.as_view({"get": "retrieve", "patch": "partial_update"}),
        name="profile",
    ),
    path(
        "session/",
        SessionViewSet.as_view(
            {"get": "list", "patch": "partial_update", "post": "create"}
        ),
        name="session",
    ),
    # path("login/", google_oauth, name="login"),  # New path for user login
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegistrationView.as_view(), name="Registration"),
]
