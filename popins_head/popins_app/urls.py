from .views import *
from django.urls import path

urlpatterns = [
    path('users/', General.as_view(), name='users'),
    path('nannies/', Nanny_api.as_view(), name='nannies'),
    path('nannies/<int:user_id>/', Nanny_api.as_view(), name='nanny_profile'),
    path('parents/', Parent_api.as_view(), name='parents'),
    path('parents/<int:user_id>/', Parent_api.as_view(), name='parent_profile'),
    path('sessions/', Session_api.as_view(), name='sessions'),
    path('sessions/<int:session_id>/', Session_api.as_view(), name='session_detail'),
    path('sessions/<int:session_id>/interests/', Session_api.as_view(), name='session_interests'),
]

