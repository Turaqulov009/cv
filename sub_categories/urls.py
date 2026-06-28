from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubCategoryViewSet

router = DefaultRouter()
router.register('subcategories', SubCategoryViewSet, basename='subcategories')

urlpatterns = [
    path('', include(router.urls)),
]