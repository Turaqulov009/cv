from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Product2ViewSet

router = DefaultRouter()
router.register('products', Product2ViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),]