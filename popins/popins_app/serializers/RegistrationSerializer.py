from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User

from ..models import Profile

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from ..models import Profile


class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    confirmed_password = serializers.CharField(write_only=True, required=True)
    is_parent = serializers.BooleanField(required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "confirmed_password",
            "is_parent",
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs["confirmed_password"]:
            raise serializers.ValidationError(
                {"confirmed_password": "Password fields don't match."}
            )
        return attrs

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        is_parent = validated_data["is_parent"]

        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        user_profile = Profile.objects.create(
            user=user, is_parent=is_parent, name=username
        )
        user_profile.save()

        return user


# from django.contrib.auth.models import User


# from rest_framework import serializers
# from rest_framework.validators import UniqueValidator
# from django.core.exceptions import ValidationError
# from django.contrib.auth.models import User
# from django.contrib.auth.password_validation import validate_password
# from ..models import Profile


# class RegistrationSerializer(serializers.ModelSerializer):
#     # email = serializers.EmailField(
#     #     required=True, validators=[UniqueValidator(queryset=User.objects.all())]
#     # )
#     username = serializers.CharField(write_only=True, required=True)
#     password = serializers.CharField(
#         write_only=True, required=True, validators=[validate_password]
#     )
#     confirm_password = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = User
#         fields = [
#             "username",
#             "password",
#             "confirm_password",
#             # "email",
#             # "first_name",
#             # "last_name",
#             "is_parent",
#             # "profile_pic",
#             # "bio",
#             # "birth_year",
#             # "address",
#             # "social",
#         ]
#         extra_kwargs = {
#             "username": {"required": True},
#             "password": {"write-only": True},
#             "confirm_password": {"write-only": True},
#             "is_parent": {"required": True},
#         }

#     def validate(self, attrs):
#         if attrs["password"] != attrs["confirm_password"]:
#             raise serializers.ValidationError(
#                 {"confirm_password": "Password fields don't match."}
#             )
#         try:
#             validate_password(attrs["password"])
#         except ValidationError as e:
#             raise serializers.ValidationError({"password": e.messages})
#         return attrs

#     def create(self, validated_data):
#         user = User.objects.create(
#             username=validated_data["username"],
#             # email=validated_data["email"],
#         )
#         user.set_password(validated_data["password"])
#         user.save()
#         user_profile = Profile.objects.create(
#             user=user,
#             is_parent=validated_data["is_parent"],
#             name=validated_data["username"],
#         )
#         user_profile.save()
#         return user
