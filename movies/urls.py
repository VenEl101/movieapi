
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import MovieViewSet, ActorViewSet, CommentVIewSet
router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('actors', ActorViewSet)
router.register('comment', CommentVIewSet, "comment")


urlpatterns = [
    path('', include(router.urls)),
    path('movies/id:int/actors/', ActorViewSet.as_view('list')),
    path('auth/', views.obtain_auth_token),
]