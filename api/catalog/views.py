from django.db.models import Count, Q, QuerySet
from rest_framework import viewsets

from .models import Catalog, Star
from .serializers import CatalogSerializer, StarSerializer


class CatalogViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CatalogSerializer
    lookup_field = 'code'
    pagination_class = None

    def get_queryset(self) -> QuerySet[Catalog]:
        return Catalog.objects.annotate(
            stars_count=Count('stars'),
            named_stars_count=Count('stars', filter=Q(stars__name__gt='')),
        )


class StarViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Star.objects.all()
    serializer_class = StarSerializer
