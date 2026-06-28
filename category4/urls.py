from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Category4ViewSet

router = DefaultRouter()
router.register('category4', Category4ViewSet, basename='category4')

urlpatterns = [
    path('', include(router.urls)),
]