from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products3', Product3ViewSet, basename='products3')

urlpatterns = [
    path('', include(router.urls)),
]