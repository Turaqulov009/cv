from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubCategory4ViewSet


router = DefaultRouter()
router.register('subcategory4', SubCategory4ViewSet, basename='subcategory4')

urlpatterns = [
    path('', include(router.urls)),
]