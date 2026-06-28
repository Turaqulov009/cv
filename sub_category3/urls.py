from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('subcategory3', SubCategory3ViewSet, basename='subcategory3')

urlpatterns = [
    path('', include(router.urls)),
]