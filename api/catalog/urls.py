from rest_framework.routers import DefaultRouter

from .views import CatalogViewSet, ConstellationViewSet, StarViewSet

router = DefaultRouter()
router.register(r'catalogs', CatalogViewSet, basename='catalog')
router.register(r'constellations', ConstellationViewSet, basename='constellation')
router.register(r'stars', StarViewSet, basename='star')

app_name = 'catalog'
urlpatterns = router.urls
