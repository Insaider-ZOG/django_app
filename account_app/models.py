from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.db import models


class MyAccountManager(BaseUserManager):

    def create_user(self, email, username, password=None, is_admin=False,
                    is_staff=False, is_superuser=False, is_active=True):

        if not email:
            raise ValueError("User mast have an email")
        if not password:
            raise ValueError("User must have a password")
        if not username:
            raise ValueError("User must have a username")

        user_obj = self.model(
            email=self.normalize_email(email),
            username=username
        )

        user_obj.set_password(password)

        user_obj.is_admin=is_admin
        user_obj.is_superuser=is_superuser
        user_obj.is_staff=is_staff
        user_obj.is_active=is_active

        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, email, username, password):

        user_obj = self.create_user(
            email,
            username,
            password=password,
        )

        user_obj.is_admin = True
        user_obj.is_staff = True
        user_obj.is_superuser = True

        user_obj.save(using=self._db)
        return user_obj


class Account(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username",)

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_lable):
        return True

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Account"
        ordering = ("date_joined", )