from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet,ProductViewSet,CategoryViewSet,UserViewSet


router = DefaultRouter()

router.register('posts', PostViewSet, basename='posts')
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSet, basename='categories')
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]