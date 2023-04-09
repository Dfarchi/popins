from django.utils import timezone
from rest_framework import serializers
from rest_framework.authtoken.admin import User

from .models import Session

from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('id', 'user', 'is_parent', 'is_nanny', 'name', 'bio', 'birth_year', 'address', 'link', 'profile_pic')



class SessionValidationSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(source='user.id', read_only=True)
    date = serializers.DateField(required=True)
    salary = serializers.IntegerField(required=True)
    note = serializers.CharField(max_length=256, required=True)
    user_name = serializers.CharField(source='user.profile.name', read_only=True)
    interested_nannys = serializers.SerializerMethodField()

    class Meta:
        model = Session
        fields = ('id', 'user_id', 'user_name', 'date', 'salary', 'has_happened', 'interested_nannys')

    def validate_user_id(self, user_id):
        if not User.objects.filter(id=user_id).exists():
            raise serializers.ValidationError("Invalid user ID.")
        return user_id

    def validate_date(self, date):
        if date < timezone.now().date():
            raise serializers.ValidationError("The date cannot be in the past.")
        return date

    def validate_salary(self, salary):
        if salary < 30:
            raise serializers.ValidationError("Salary cannot be under 30NIS.")
        return salary

    def get_interested_nannys(self, session):
        return [{'id': nanny.id, 'name': nanny.profile.name} for nanny in session.interested_nannys.all()]


class InterestValidationSerializer(serializers.Serializer):
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
        if not User.objects.filter(id=nanny).exists():
            raise serializers.ValidationError("Invalid user ID.")
        return nanny


class ReviewValidationSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(source='user.id', read_only=True)
    date = serializers.DateField(required=True)

    def validate_user_id(self, user_id):
        if not User.objects.filter(id=user_id).exists():
            raise serializers.ValidationError("Invalid user ID.")
        return user_id

    def validate_date(self, date):
        if date < timezone.now().date():
            raise serializers.ValidationError("The date cannot be in the past.")
        return date
