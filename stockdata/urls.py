from django.urls import path, include
from rest_framework.routers import DefaultRouter

from stockdata import views


router = DefaultRouter()
router.register('stockdata', views.StocksViewSet)

urlpatterns = [
    path('', include(router.urls)),
]