import secrets

from rest_framework import serializers
from .models import User, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'unique', 'token']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'unique', 'password']

    def create(self, validated_data):
        token = secrets.token_urlsafe(32)  # Увеличенная длина для большей уникальности
        unique_token = False
        while not unique_token:
            if not User.objects.filter(token=token).exists():
                unique_token = True
            else:
                token = secrets.token_urlsafe(32)  # Повторная генерация, если токен не уникален

        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            unique=validated_data['unique'],
            password=validated_data['password']
        )
        user.token = token
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class MessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.ReadOnlyField(source='sender.username')
    recipient_username = serializers.ReadOnlyField(source='recipient.username')

    class Meta:
        model = Message
        fields = ['id', 'sender_username', 'recipient_username', 'content', 'created_at', 'delivered']


class UpdateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def update(self, instance, validated_data):
        if 'username' in validated_data:
            instance.username = validated_data['username']
        if 'email' in validated_data:
            instance.email = validated_data['email']
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance