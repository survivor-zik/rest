from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
@csrf_exempt
def registeredUsers(request):
    if request.method =='GET':
        user=User.objects.all()
        serializer=UserSerializer(user,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method =='POST':
        data= JSONParser().parse(request)
        serializer=UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors,status=400)

            