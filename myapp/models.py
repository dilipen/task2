"""
All Model should be an sql table.
"""

# import uuid
from django.utils import timezone

# from django.contrib.auth.models import User
# from django.contrib.auth.validators import ASCIIUsernameValidator

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Cob(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)


class Corporate(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class MainBranch(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    corporate = models.ForeignKey(Corporate, null=True, blank=True, on_delete=models.CASCADE)  # NOQA


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    main_branch = models.ForeignKey(MainBranch, null=True, blank=True, on_delete=models.CASCADE)  # NOQA


class SubDomain(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)  # NOQA


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    sub_domain = models.ForeignKey(SubDomain, null=True, blank=True, on_delete=models.CASCADE)  # NOQA
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)  # NOQA
    roles = models.ManyToManyField(Role)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    @staticmethod
    def has_perm(self, perm, obj=None):
        return True

    @staticmethod
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    sub_domain = models.ForeignKey(SubDomain, null=True, blank=True, on_delete=models.CASCADE)  # NOQA


class UserNotification(models.Model):
    id = models.AutoField(primary_key=True)
    notification = models.ForeignKey(Notification, null=True, blank=True, on_delete=models.CASCADE)  # NOQA
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)  # NOQA
    has_readed_at = models.BooleanField(blank=True, default=False)
    readed_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
