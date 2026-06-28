from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Category3ViewSet

router = DefaultRouter()
router.register('category3', Category3ViewSet, basename='category3')

urlpatterns = [
    path('', include(router.urls)),
]