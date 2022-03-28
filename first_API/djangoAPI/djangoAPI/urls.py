from os import name
from typing import List
from django.contrib import admin
from django.urls import path, include
from apiApp.views import ListView, UserViewset
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('list', ListView, basename='listview')
router.register('api/tutorials/<int:pk>', ListView, basename='listview')
router.register('users', UserViewset, basename='users')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('apidet/', include(router.urls)),
    path('api/token/', obtain_auth_token, name='obtain')
]
