from django.urls.conf import include
from rest_framework import routers
from django.contrib import admin
from django.urls import path
from .import views

router = routers.SimpleRouter()
router.register('likes', views.UserPosts, basename='UserPosts')
router.register('comment', views.comment, basename='comment')

urlpatterns = [
    path('',include(router.urls)),
    path('PostLIke',views.PostLIke.as_view(),name='PostLIke'),
    # path('UserRegistration',views.UserRegistration.as_view(),name='UserRegistration'),
   
]