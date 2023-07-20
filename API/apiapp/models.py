from django.db import models
from django.core.validators import MinLengthValidator,EmailValidator
from datetime import datetime


# Create your models here.
class User(models.Model):
    username=models.CharField(primary_key=True,auto_created=False)
    name = models.CharField(max_length=100,null=True,validators=[MinLengthValidator(8)])
    email = models.EmailField(null=False,validators=[EmailValidator()])
    password = models.CharField(max_length=100,null=False)
    age=models.IntegerField(null=True)
    datejoined=models.DateTimeField(auto_created=True,default=datetime.now())
    
    def __str__(self):
        return self.name
    

