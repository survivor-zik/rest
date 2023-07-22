# from django.contrib import admin
from django.urls import path,include
# from apiapp.views import index
from .views import index,registeredUsers

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',index),
    
    path('total_users/',registeredUsers),
    # path('logout'),
    # path('register'),
    # path('user'),
]