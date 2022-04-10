from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'register' 

router = DefaultRouter()
router.register('', views.ViewRP, basename="RP")

urlpatterns = [
    path('',views.Signup.as_view()),
    path('user', include(router.urls)),
    path('signup/',views.Signup.as_view(), name = 'signup'),
    # path('save/',views.Save.as_view(), name = 'save'),
]