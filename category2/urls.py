from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .models import Category2
from .views import Category2ViewSet


router = DefaultRouter()
router.register('category2', Category2ViewSet, basename='category2')

urlpatterns = [
    path('', include(router.urls)),
]