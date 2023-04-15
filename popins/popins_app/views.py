from django.http import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .models import *
from .serializers import *


#######EXAMPLE############

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


class NanniesList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        nannies = Profile.objects.filter(is_nanny=True)
        serializer = ProfileSerializer(nannies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Nannysingle(APIView):
    """
    Retrieve, update or delete a single Nanny instance.
    """
    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        nanny = self.get_object(pk)
        serializer = ProfileSerializer(nanny)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        nanny = self.get_object(pk)
        serializer = ProfileSerializer(nanny, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        nanny = self.get_object(pk)
        nanny.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ParentsList(APIView):
    """
    List all Parents, or create a new Parent Profile.
    """
    def get(self, request, format=None):
        parents = Profile.objects.filter(is_parent=True)
        serializer = ProfileSerializer(parents, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Parentsingle(APIView):
    """
    Retrieve, update or delete a single Parent instance.
    """
    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        parent = self.get_object(pk)
        serializer = ProfileSerializer(parent)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        parent = self.get_object(pk)
        serializer = ProfileSerializer(parent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        parent = self.get_object(pk)
        parent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SessionsList(APIView):
    """
    List all Sessions by date, or create a new Session.
    """
    def get(self, request, format=None):
        sessions = Session.objects.filter(date=request.data.date)
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Sessionsingle(APIView):
    """
    Retrieve, update or delete a single Session instance.
    """
    def get_object(self, pk):
        try:
            return Session.objects.get(pk=pk)
        except Session.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        session = self.get_object(pk)
        serializer = SessionSerializer(session)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        session = self.get_object(pk)
        serializer = SessionSerializer(session, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        session = self.get_object(pk)
        session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class Session_api(APIView):
#
#     def get_sessions(self):
#         """for admin reasons"""
#         all_sessions = Session.objects.all()
#         return Response(all_sessions)
#
#     def get_session_by_user_id(self, user_id):
#         all_sessions = [session for session in Session.objects.all if Session.user == user_id]
#         happend = [session for session in all_sessions if session.has_happened]
#
#         return all_sessions
#
#     def get_session_by_id(self, session_id) -> Session:
#         return get_object_or_404(Session, id=session_id)
#
#     def get_session_interests(self, sessions_id) -> Response:
#         """when a parent wants to see all the interests different nannies had for their session"""
#         interests_list = []
#         for interest in Interest.objects.all().filter(session =sessions_id):
#             interests_list.append({
#                 'name': interest.nanny,  # this should be a link to Nanny_api.get_profile(self, user_id)
#                 'note': interest.note,
#                 'talked': interest.talked,
#                 'status': interest.status
#             })
#         return Response(interests_list)
#
#     def update_session_has_happened(self,session_id):
#         se = self.get_session_by_id(session_id)
#         se.has_happened = True

class InterestsList(APIView):
    """
    List all Interests, or create a new Interest.
    """
    def get(self, request, format=None):
        interest = Interest.objects.all()
        serializer = InterestSerializer(interest, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InterestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Interestsingle(APIView):
    """
    Retrieve, update or delete a single Interest instance.
    """
    def get_object(self, pk):
        try:
            return Interest.objects.get(pk=pk)
        except Interest.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        interest = self.get_object(pk)
        serializer = InterestSerializer(interest)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        interest = self.get_object(pk)
        serializer = InterestSerializer(interest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        interest = self.get_object(pk)
        interest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class Interest_api(APIView):
#
#     def get_sessions(self):
#         """for admin reasons"""
#         all_interest = Interest.objects.all()
#         return Response(all_interest)
#
#     def get_interest_by_id(self, interest_id) -> Interest:
#         return get_object_or_404(Interest, id=interest_id)
#
#     def update_had_talked(self, sessions_id):
#         """when talked checkbox had been checked"""
#         interest = self.get_interest_by_id(sessions_id)
#         interest.talked = True
#     def update_status(self, sessions_id):
#         """when session bean sealed checkbox had been checked"""
#         interest = self.get_interest_by_id(sessions_id)
#         interest.status = True


# list of functions I will need at some point

class ReviewsList(APIView):
    """
    List all Reviews, or create a new Review.
    """
    def get(self, request, format=None):
        review = Review.objects.filter(is_nanny=True)
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Reviewsingle(APIView):
    """
    Retrieve, update or delete a single Review instance.
    """
    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        review = self.get_object(pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)