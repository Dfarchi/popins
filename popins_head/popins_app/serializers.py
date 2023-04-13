from abc import ABC
from django.utils import timezone
from rest_framework.authtoken.admin import User
from .models import *
from rest_framework import serializers

def validate_user_id(user_id):
    if not User.objects.filter(id=user_id).exists():
        raise serializers.ValidationError("Invalid user ID.")
    return user_id

def validate_date(value):
    if value < timezone.now().date():
        raise serializers.ValidationError("The date cannot be in the past.")
    return value

def validate_salary(value):
    if value < 30:
        raise serializers.ValidationError("Salary cannot be under 30NIS.")
    return value


class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id', read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'is_parent', 'is_nanny', 'name', 'bio', 'birth_year', 'address', 'link', 'profile_pic')



class SessionValidationSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id', read_only=True)
    date = serializers.DateField(required=True)
    salary = serializers.IntegerField(required=True)
    note = serializers.CharField(max_length=256, required=True)
    user_name = serializers.CharField(source='user.profile.name', read_only=True)
    interested_nannies = serializers.SerializerMethodField()

    class Meta:
        model = Session
        fields = ('id', 'user_id', 'user_name', 'date', 'salary', 'has_happened', 'interested_nannies')

    def validate_user_id(self, value):
        return validate_user_id(value)

    def validate_date(self, value):
        return validate_date(value)

    def validate_salary(self, value):
        return validate_salary(value)

    # def get_interested_nannys(self, session):
    #     return [{'id': nanny.id, 'name': nanny.profile.name} for nanny in session.interested_nannys.all()]


class InterestValidationSerializer(serializers.ModelSerializer):
    nanny = serializers.IntegerField(source='user.id', read_only=True)
    session = serializers.IntegerField(source='sessions.id', read_only=True)
    note = serializers.CharField(max_length=256, required=True)
    user_name = serializers.CharField(source='user.profile.name', read_only=True)

    class Meta:
        model = Session
        fields = ('id', 'session', 'user_id', 'user_name', 'note',  'talked', 'status')

    def validate_session_id(self, session):
        if not Session.objects.filter(id=session).exists():
            raise serializers.ValidationError("Invalid session ID.")
        return session

    def validate_nanny_id(self, nanny):
        return validate_user_id(nanny)


class ReviewValidationSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id', read_only=True)
    date = serializers.DateField(required=True)

    # def validate_user_id(self, value):
    #     return validate_user_id(value)
    #
    # def validate_date(self, value):
    #     return validate_date(value)