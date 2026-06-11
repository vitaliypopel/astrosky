from datetime import datetime, timezone

from django.db.models import Count, Q, QuerySet
from engine import calculate_altaz
from rest_framework import views, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Catalog, Star
from .serializers import CatalogSerializer, StarSerializer


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


class StarViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Star.objects.all()
    serializer_class = StarSerializer


class AlzAzAPIView(views.APIView):
    def get(self, request: Request) -> Response:
        result = calculate_altaz(
            ra_h=float(request.GET['ra']),
            dec_deg=float(request.GET['dec']),
            lat_deg=float(request.GET['lat']),
            lon_deg=float(request.GET['lon']),
            dt=datetime.now(timezone.utc),
        )

        return Response(result)
