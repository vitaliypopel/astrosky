from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AlzAzAPIView, CatalogViewSet, StarViewSet

router = DefaultRouter()
router.register(r'catalogs', CatalogViewSet, basename='catalog')
router.register(r'stars', StarViewSet, basename='star')

app_name = 'catalog'
urlpatterns = [
    path('', include(router.urls)),
    path('altaz/', AlzAzAPIView.as_view(), name='altaz'),
]
