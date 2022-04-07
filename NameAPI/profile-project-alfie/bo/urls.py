from django.urls import path
from . import views, movies

app_name = 'bo' 

urlpatterns = [
    path('',views.View.as_view()),
    path('user/',views.View.as_view(), name='user'),
    path('user/list/',views.Transact.as_view(), name='user-list'),
    path('user/save/<int:pk>/',views.Transact.as_view(), name='user-save'),
    path('movies/',movies.Movies.as_view(), name='movies'),



]