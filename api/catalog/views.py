from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Constellation, Star
from .serializers import ConstellationSerializer, StarSerializer


class ConstellationViewSet(ReadOnlyModelViewSet):
    queryset = Constellation.objects.all()
    serializer_class = ConstellationSerializer
    pagination_class = None


class StarViewSet(ReadOnlyModelViewSet):
    queryset = Star.objects.select_related('constellation').order_by('pk')
    serializer_class = StarSerializer
