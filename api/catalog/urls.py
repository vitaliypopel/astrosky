from rest_framework.routers import DefaultRouter

from .views import ConstellationViewSet, StarViewSet

router = DefaultRouter()
router.register(r'constellations', ConstellationViewSet, basename='constellation')
router.register(r'stars', StarViewSet, basename='star')

app_name = 'catalog'
urlpatterns = router.urls
