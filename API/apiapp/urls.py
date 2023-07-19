# from django.contrib import admin
from django.urls import path,include
# from apiapp.views import index
from .views import index

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',index),
]