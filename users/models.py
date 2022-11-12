from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.files.storage import FileSystemStorage

class User(AbstractUser):
    is_member = models.BooleanField(default=False)
    is_guide = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    create_datetime = models.DateTimeField(auto_now=True, auto_now_add=False)
    update_datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_login = models.DateTimeField(auto_now=False, auto_now_add=True)
    
class Member(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    allergic = models.CharField(max_length=100)
    underlying_disease = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    member_image = models.ImageField(null = True, blank = True,upload_to="images/member/")
    
class Guide(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    detail = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    province = models.CharField(max_length=100)
    tat_license = models.CharField(max_length=100)
    guide_image = models.ImageField(null = True, blank = True,upload_to="images/guide/")

