from django.db.models import Count, Q, QuerySet
from rest_framework import viewsets

from .models import Catalog, Constellation, Star
from .serializers import (
    CatalogSerializer,
    ConstellationSerializer,
    StarSerializer,
)


class CatalogViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CatalogSerializer
    lookup_field = 'code'
    pagination_class = None

    def get_queryset(self) -> QuerySet[Catalog]:
        return Catalog.objects.annotate(
            stars_count=Count('stars'),
            named_stars_count=Count(
                'stars',
                filter=Q(stars__name__isnull=False) & ~Q(stars__name=''),
            ),
        )


class ConstellationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Constellation.objects.all()
    serializer_class = ConstellationSerializer
    pagination_class = None


class StarViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = (
        Star.objects.select_related('catalog')
        .select_related('constellation')
        .order_by('pk')
    )
    serializer_class = StarSerializer
