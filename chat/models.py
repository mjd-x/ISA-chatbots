from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            password=password,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        return self._create_user(username, email, password, is_staff, is_superuser, **extra_fields)

    def create_superuser(self, username, email, password, is_staff, is_superuser, **extra_fields):
        return self.create_user(username, email, password, is_staff, is_superuser, **extra_fields)


class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=40, null=True)
    email = models.EmailField(max_length=255, unique=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    class Meta:
        abstract: True

    USERNAME_FIELD = 'username'

    def natural_key(self):
        return self.username

    def __str__(self):
        return self.username

class Person(User):
    pass

class Bot(User):
    botInstance = models.IntegerField(null=True, unique=True)

    def __init__(self, *args, **kwargs):
        super().__init__(password=self.set_unusable_password(), email=None, *args, **kwargs)

class Chat(models.Model):
    idUser1 = models.ForeignKey(User, related_name='idUser1', on_delete=models.CASCADE, null=True)
    idUser2 = models.ForeignKey(User, related_name='idUser2', on_delete=models.CASCADE, null=True)

    def __str__(self):
        string = str(self.idUser1) + " + " + str(self.idUser2)
        return string

class Message(models.Model):
    message = models.CharField(max_length=255, null=True)
    idUser = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(null=True, auto_now_add=True)
    idChat = models.ForeignKey(Chat, on_delete=models.CASCADE, null=True)

    def __str__(self):
        #string= "(" + str(self.idChat.id) + ") " + str(self.idUser) + ": " + '"' + str(self.message) + '"'
        string = str(self.idUser) + ": " + '"' + str(self.message) + '"'
        return string