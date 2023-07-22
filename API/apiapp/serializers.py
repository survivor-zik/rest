from rest_framework import serializers
from .models import User
from django.core.validators import MinLengthValidator, EmailValidator
from datetime import datetime
from rest_framework.authtoken.views import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=['username','name','email','password','age','datejoined']
        
        