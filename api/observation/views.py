from engine import observe, observe_many
from engine.models import Observer, StellarObject
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import (
    ObservationSerializer,
    ObserveManySerializer,
    ObserveSerializer,
)


class ObserveAPIView(GenericAPIView):
    serializer_class = ObserveSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        observation = observe(
            Observer(**data['observer']),
            StellarObject(**data['obj']),
            data['dt'],
        )

        return Response(ObservationSerializer(observation).data)


class ObserveManyAPIView(GenericAPIView):
    serializer_class = ObserveManySerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        observation = observe_many(
            Observer(**data['observer']),
            [StellarObject(**obj) for obj in data['objects']],
            data['dt'],
        )

        return Response(ObservationSerializer(observation).data)
