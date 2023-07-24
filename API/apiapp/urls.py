# from django.contrib import admin
from django.urls import path,include
# from apiapp.views import index
from .views import index,registerUsers,user_details,login

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',index),
    path('usereg/',registerUsers),
    path('userdetails/<str:username>/',user_details),
    path('login/',login),
    # path('register'),
    # path('user'),
]