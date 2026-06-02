from django.urls import path

from .views import CatalogViewSet, StarViewSet

app_name = 'catalog'
urlpatterns = [
    path(
        'catalogs/',
        CatalogViewSet.as_view({'get': 'list'}),
        name='catalog-list',
    ),
    path(
        'catalogs/<slug:code>/',
        CatalogViewSet.as_view({'get': 'retrieve'}),
        name='catalog-detail',
    ),
    path(
        'catalogs/<slug:code>/stars/',
        StarViewSet.as_view({'get': 'list'}),
        name='catalog-star-list',
    ),
    path(
        'catalogs/<slug:code>/stars/<int:source_id>/',
        StarViewSet.as_view({'get': 'retrieve'}),
        name='catalog-star-detail',
    ),
]
