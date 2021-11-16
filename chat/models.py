from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, username, password, **extra_fields):
        values = [email, username]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField()
    username = models.CharField(max_length=150, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
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