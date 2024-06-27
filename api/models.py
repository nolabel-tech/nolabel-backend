import secrets

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, username, unique, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        if not unique:
            raise ValueError('Users must have a unique identifier')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            unique=unique
        )

        user.set_password(password)
        user.token = user.generate_unique_token()
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, unique, password):
        user = self.create_user(
            email=email,
            username=username,
            unique=unique,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)  # Убедитесь, что username также уникален
    unique = models.CharField(max_length=255, unique=True)
    token = models.CharField(max_length=255, unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'  # Изменено на username
    REQUIRED_FIELDS = ['email', 'unique']  # Email теперь в списке обязательных полей

    def __str__(self):
        return self.username  # Возвращаем username вместо email

    def generate_unique_token(self):
        while True:
            token = secrets.token_urlsafe(32)
            if not User.objects.filter(token=token).exists():
                return token


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"From {self.sender.username} to {self.recipient.username}"
