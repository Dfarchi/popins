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

class UserList(APIView):
    """
    List all users, or create a new user.
    """
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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