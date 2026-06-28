from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('subcategory2', SubCategory2ViewSet, basename='subcategory2')

urlpatterns = [
    path('', include(router.urls)),
]