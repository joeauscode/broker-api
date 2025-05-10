
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Account
from . utils import SendMail


# Serializer for built-in User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


# Main serializer for Account model
class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested user info

    class Meta:
        model = Account
        fields = [
            'user', 'first_name', 'last_name', 'phone',
            'email', 'gender', 'balance', 'created'
        ]


# Registration serializer (creates both User and Account)
class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Account
        fields = [
            'first_name', 'last_name', 'username', 'email',
            'password1', 'password2', 'phone', 'gender', 'balance'
        ]

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError('Username already exists')
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError('Email already exists')
        if Account.objects.filter(phone=data['phone']).exists():
            raise serializers.ValidationError('Phone number already exists')
        return data

    def create(self, validated_data):
        # Extract user data
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password1')
        validated_data.pop('password2')

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)

        # Create account and link to user
        account = Account.objects.create(
            user=user,
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            phone=validated_data.get('phone'),
            email=email,
            gender=validated_data.get('gender'),
            balance=validated_data.get('balance'),
        )

     
        SendMail(email,account.fullname)
        return account