from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views.Session_viewset import SessionViewSet

from .views.Register_viewset import RegistrationView

from .views.Profile_viewset import ProfileView

router = DefaultRouter()
router.register(r"profile", viewset=ProfileView)
router.register(r"session", viewset=SessionViewSet)


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegistrationView.as_view(), name="Registration"),
] + router.urls
# path("login/", google_oauth, name="login"),  # New path for user login
# path("auth/google-oauth/", google_oauth, name="google-oauth"),
# path(
#     "profile/",
#     ProfileView.as_view({"get": "retrieve", "patch": "partial_update"}),
#     name="profile",
# ),
# path(
#     "session/",
#     SessionViewSet.as_view(
#         {"get": "list", "patch": "partial_update", "post": "create"}
#     ),
#     name="session",
# ),
