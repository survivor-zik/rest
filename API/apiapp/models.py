from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, EmailValidator
from django.utils import timezone
from django.db import models
from django.core.validators import MinLengthValidator,EmailValidator
from datetime import datetime


# Create your models here.
class User(models.Model):
    username=models.CharField(primary_key=True,auto_created=False)
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=False,validators=[EmailValidator()],unique=True)
    password = models.CharField(max_length=100,null=False,validators=[MinLengthValidator(8)])
    age=models.IntegerField(null=True)
    datejoined=models.DateTimeField(auto_created=True,default=datetime.now())
    
    def __str__(self):
        return self.username
    
    
    
    