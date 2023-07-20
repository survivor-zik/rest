from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.

def registeredUsers(request):
    if request.method =='GET':
        user=User.objects.all()
        serializer=UserSerializer(user,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method =='POST':
        data= JSONParser().parse(request)