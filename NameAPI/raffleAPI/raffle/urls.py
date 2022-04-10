from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'raffle' 

router = DefaultRouter()
router.register('', views.ViewRP, basename="RP")

urlpatterns = [
    # path('',views.Signup.as_view()),
    path('user1', include(router.urls)),
]