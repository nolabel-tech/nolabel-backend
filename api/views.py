from rest_framework.views import APIView
from .models import User, Message
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, MessageSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"token": user.token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# api/views.py

from django.contrib.auth import authenticate, get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                if user.is_active:
                    # Пользователь успешно аутентифицирован
                    return Response({"token": user.token}, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Account is disabled."}, status=status.HTTP_403_FORBIDDEN)
            else:
                print(password)
                # Неправильный пароль
                return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            # Пользователь не найден
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


class ContactView(APIView):
    def post(self, request):
        try:
            user = User.objects.get(username=request.data.get('username'), email=request.data.get('email'))
            return Response({"unique": user.unique}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


class SendMessageView(APIView):
    def post(self, request):
        recipient_unique = request.data.get('unique')
        message_content = request.data.get('message')
        from_user_unique = request.data.get('from_user')

        try:
            recipient = User.objects.get(unique=recipient_unique)
            from_user = User.objects.get(unique=from_user_unique)
            # Создаем сообщение в базе данных
            message = Message.objects.create(
                sender=from_user,
                recipient=recipient,
                content=message_content
            )
            # Логика доставки сообщения
            # Например, можно отправить HTTP запрос на клиентское приложение получателя, если оно поддерживает такой прием
            # Здесь может быть интеграция с внешним сервисом или использование существующих клиентских соединений
            # Эмулируем доставку:
            message.delivered = True
            message.save()
            return Response(
                {"message": "Message sent successfully", "from": from_user.username, "to": recipient.username},
                status=200)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)


class CheckMessagesView(APIView):
    def get(self, request, unique):
        try:
            user = User.objects.get(unique=unique)
            messages = Message.objects.filter(recipient=user, delivered=False)
            messages.update(delivered=True)  # Помечаем сообщения как доставленные
            serializer = MessageSerializer(messages, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
