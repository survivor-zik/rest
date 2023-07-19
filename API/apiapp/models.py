from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(primary_key=True,auto_created=False)
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=100,null=False)
    age=models.IntegerField(null=True)
    
    
    
