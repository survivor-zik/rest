from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import User
import logging
from datetime import datetime
logger = logging.getLogger('apiapp')
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password, check_password
from .serializers import UserSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions 

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@api_view(['POST'])
def registerUsers(request):
    if request.method =='POST':
        data=request.data
        password = data.get('password')
        hashed_password = make_password(password)
        data['password'] = hashed_password
        serializer=UserSerializer(data=data)
        logging.info(f"""registration attempt {datetime.now()} with credentials {data['username']} """)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'User registered successfully',
                'username': serializer.data['username'],
            }
            logging.info(f"""User with username {data['username']} at {datetime.now()} """)
            return Response(response_data, status=status.HTTP_201_CREATED)
        logging.warning(f"""Invalid Issues {status.HTTP_400_BAD_REQUEST}""")
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def user_details(request,username):
    try:
        user=User.objects.get(username=username)
    except User.DoesNotExist:
        # print(username)
        logging.warning(f"""Invalid Credentials at {datetime.now()} with username {username} """)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method =='GET':
        response_data = {
                
                'username': username,
                'status':status.HTTP_200_OK,
            }
        logging.info(f"""Details delivered {datetime.now()} of username {username}""")
        return Response(response_data)
    elif request.method == 'PUT':
        data = request.data
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            logging.warning(f"Invalid Credentials at {datetime.now()} with username {username}")
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # Update serializer data with the password if present
        password = data.get('password')
        if password:
            if not check_password(password, user.password):
                hashed_password = make_password(password)
                data['password'] = hashed_password

        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'User Updated successfully',
                'username': username,
            }
            logging.info(f"Details updated {datetime.now()} of username {username}")
            return Response(response_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method =='DELETE':
        user.delete()
        response_data = {
                'message': 'User Deleted successfully',
                'username': username,
            }
        logging.info(f"""Details deleted {datetime.now()} of username {username}""")
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