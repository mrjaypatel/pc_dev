from django.db import models

# Create your models here.
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(self, phone_no, password=None, **extra_fields):
        if not phone_no:
            raise ValueError('Phone number is required')
        extra_fields['email'] = self.normalize_email(extra_fields['email'])
        user = self.model(phone_no=phone_no, **extra_fields)
        hashPwd = make_password(password)
        user.set_password(hashPwd)
        user.save(using=self.db)
        return user

    def create_superuser(self, phone_no, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        self.create_user(phone_no, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    full_name = models.CharField(max_length=50, blank=True, null=True)
    phone_no = models.CharField(
                                    max_length=10,
                                    blank=True,
                                    null=True,
                                    unique=True
                                )
    email = models.EmailField(unique=True)
    profile = models.CharField(max_length=500, blank=True, null=True)
    USERNAME_FIELD = 'phone_no'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.phone_no


class NotesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class Note(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    is_deleted = models.BooleanField(default=False)
    objects = NotesManager()
    admin_objects = models.Manager()


class Status(models.Model):
    title = models.CharField(max_length=150)


class PersonalInfo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    address = models.TextField()
    is_deleted = models.BooleanField(default=False)


class Role(models.Model):
    title = models.CharField(max_length=150)
    permissions = models.TextField()
    is_deleted = models.BooleanField(default=False)


class Group(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    max_users = models.IntegerField()
    subscription_amt = models.IntegerField()
    penalty_amt = models.IntegerField()
    is_deleted = models.BooleanField(default=False)


class Subscription(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    subscription_no = models.CharField(max_length=10)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.subscription_no    


class Investment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, null=True,blank=True)
    total_invested = models.IntegerField()
    total_owe = models.IntegerField()
    total_penalty = models.IntegerField()
    total_penalty_owe = models.IntegerField()
    check_in_date = models.DateTimeField(blank=True, null=True)
    check_out_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)


class Draw(models.Model):
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE)
    winning_amt = models.IntegerField()
    draw_date = models.DateTimeField(blank=True, null=True)
    pre_edge_winner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='draw_pre_winner')
    post_edge_winner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='draw_post_winner')
