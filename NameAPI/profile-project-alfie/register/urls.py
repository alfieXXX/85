from django.urls import path
from . import views

app_name = 'register' 

urlpatterns = [
    path('',views.Signup.as_view()),
    path('signup/',views.Signup.as_view(), name = 'signup'),
    path('save/',views.Save.as_view(), name = 'save'),


]