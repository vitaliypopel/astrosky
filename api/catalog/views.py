from rest_framework import viewsets

from .models import Catalog, Star
from .serializers import CatalogSerializer, StarSerializer


class CatalogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    lookup_field = 'code'


class StarViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Star.objects.all()
    serializer_class = StarSerializer
