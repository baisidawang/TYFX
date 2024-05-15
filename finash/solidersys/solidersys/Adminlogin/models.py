from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# class User(models.Model):
#     student_id = models.CharField(max_length=10)
#     password = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.student_id


# class UserInfo(models.Model):
#     username = models.CharField(max_length=150, unique=True)
#     password = models.CharField(max_length=150)
#     class Meta:
#         verbose_name = '后台登录信息表'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name
# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError('The username must be set')
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         return self.create_user(username, password, **extra_fields)
#
#
# class CustomUser(AbstractBaseUser):
#     username = models.CharField(max_length=150, unique=True)
#     password = models.CharField(max_length=150)
#     # 在这里添加其他你需要的用户信息字段
#
#     objects = CustomUserManager()
#
#     USERNAME_FIELD = 'username'
#
#     def __str__(self):
#         return self.username
