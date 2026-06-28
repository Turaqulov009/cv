from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CatigoriesViewSet  # yoki qanday nom bergan bo'lsang

router = DefaultRouter()
router.register('categories', CatigoriesViewSet, basename='categories')



urlpatterns = [
    path('', include(router.urls)),
]

