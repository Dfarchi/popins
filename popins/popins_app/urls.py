from . import views
from .views import *
from django.urls import path




urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('nannies/', NanniesList.as_view(), name='nannies'),
    path('nannies/<int:pk>/', Nannysingle.as_view(), name='nanny'),
    path('parents/', ParentsList.as_view(), name='parents'),
    path('parents/<int:pk>/', Parentsingle.as_view(), name='parent'),
    path('sessions/', SessionsList.as_view(), name='sessions'),
    path('sessions/<int:pk>/', Sessionsingle.as_view(), name='session'),
    path('interests/', InterestsList.as_view(), name='interests'),
    path('interests/<int:pk>/', Interestsingle.as_view(), name='interest'),
    path('reviews/', ReviewsList.as_view(), name='reviews'),
    path('reviews/<int:pk>/', Reviewsingle.as_view(), name='review'),
]