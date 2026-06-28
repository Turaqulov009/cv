from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products4.views import Products4ViewSet

router = DefaultRouter()
router.register('products4', Products4ViewSet, basename='products4')

urlpatterns = [
    path('', include(router.urls)),
]