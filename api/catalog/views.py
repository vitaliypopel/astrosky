from django.db.models.query import QuerySet
from rest_framework import viewsets

from .models import Catalog, Star
from .serializers import CatalogSerializer, StarSerializer


class CatalogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    lookup_field = 'code'


class StarViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StarSerializer
    lookup_field = 'source_id'

    def get_queryset(self) -> QuerySet[Star]:
        return Star.objects.filter(catalog__code=self.kwargs['code'])
