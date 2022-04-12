from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.contrib import admin



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("APIapp.urls"))
]