from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import User
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password, check_password
from .serializers import UserSerializer
from rest_framework.parsers import JSONParser
# from django.views.decorators import api_view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
@api_view(['POST'])
def registerUsers(request):
    if request.method =='POST':
        data=request.data
        password = data.get('password')
        hashed_password = make_password(password)
        data['password'] = hashed_password
        serializer=UserSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'User registered successfully',
                'username': serializer.data['username'],
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def user_details(request,username):
    try:
        user=User.objects.get(username=username)
    except User.DoesNotExist:
        print(username)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method =='GET':
        serializer=UserSerializer(user)
        response_data = {
                
                'username': username,
                'status':status
            }
        return Response(response_data)
    elif request.method =='PUT':
        data=JSONParser().parse(request)
        serializer=UserSerializer(user,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'User Updated successfully',
                'username': username,
            }
            return Response(response_data,status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        user.delete()
        response_data = {
                'message': 'User Deleted successfully',
                'username': username,
            }
        return Response(response_data,status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        data = request.data
        username = data.get('username')
        password = data.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'message': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)

        if check_password(password, user.password):
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


