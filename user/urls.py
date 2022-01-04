from django.urls.conf import include
from rest_framework import routers
from django.contrib import admin
from django.urls import path
from .import views

router = routers.SimpleRouter()
router.register('', views.Users, basename='Users')

urlpatterns = [
    path('api/',include(router.urls)),
    path('UserRegistration',views.UserRegistration.as_view(),name='UserRegistration'),
    path('UserLogin',views.UserLogin.as_view(),name='UserLogin'),
    path('profileupload',views.profileupload.as_view(),name='profileupload'),
    # path('Users',views.Users.as_view(),name='Users'),
]

