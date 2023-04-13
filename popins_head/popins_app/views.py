from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .models import *


def get_spec_user(user_id) -> User:
    return get_object_or_404(User, id=user_id)


def get_spec_profile(user_id) -> Profile:
    return get_object_or_404(Profile, id=user_id)


class General(APIView):
    # """
    # View to list all users in the system.
    #
    # * Requires token authentication.
    # * Only admin users are able to access this view.
    # """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    #
    def get_all_users(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)



#url == nannay_api/

class Nanny_api(APIView):
    def get_all_nannies(self) -> Response:
        all_nannys = [profile for profile in Profile.objects.all() if profile.is_nanny]
        return Response(all_nannys)
    def get_profile(self, user_id):
        nanny = get_spec_profile(user_id)
        if nanny.is_nanny:
            nanny_profile = {
               'name': nanny.name,
                'bio': nanny.bio,
                'pic':nanny.profile_pic
            }
            return Response(nanny_profile)
        return Response(None, 404)


#url == parent_api\

class Parent_api(APIView):

    def get_all_parents(self):
        all_parents = [profile for profile in Profile.objects.all() if profile.is_parent]
        return Response(all_parents)

    def get_profile(self, user_id):
        parent = get_spec_profile(user_id)
        if parent.is_parent:
            parent_profile = {
                'name': parent.name,
                'bio': parent.bio,
                'pic': parent.profile_pic
            }
            return Response(parent_profile)
        return Response(None, 404)

#url == session_api\

class Session_api(APIView):

    def get_sessions(self):
        """for admin reasons"""
        all_sessions = Session.objects.all()
        return Response(all_sessions)

    def get_session_by_user_id(self, user_id):
        all_sessions = [session for session in Session.objects.all if Session.user == user_id]
        happend = [session for session in all_sessions if session.has_happened]

        return all_sessions

    def get_session_by_id(self, session_id) -> Session:
        return get_object_or_404(Session, id=session_id)


    def get_session_interests(self, sessions_id) -> Response:
        """when a parent wants to see all the interests different nannies had for their session"""
        interests_list = []
        for interest in Interest.objects.all().filter(session__iexact=sessions_id):
            interests_list.append({
                'name': interest.nanny,  #this should be a link to Nanny_api.get_profile(self, user_id)
                'note': interest.note,
                'talked': interest.talked,
                'status': interest.status
            })
        return Response(interests_list)




#list of functions I will need at some point
def sign_Up():
    pass


def create_nanny_profile():
    pass


def create_parent_profile():
    pass


def create_session():
    pass


def create_interest():
    pass


def create_review():
    pass


def update_profile():
    pass


def update_session():
    pass


def update_interest():
    pass


def update_reviwe():
    pass


def get_all_interests():
    pass


def get_reviews():
    pass
