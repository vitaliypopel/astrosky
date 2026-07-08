from django.utils import timezone
from rest_framework import serializers


class ObserverSerializer(serializers.Serializer):
    lat = serializers.FloatField()
    lon = serializers.FloatField()


class CelestialObjectSerializer(serializers.Serializer):
    ra = serializers.FloatField()
    dec = serializers.FloatField()


class ObserveSerializer(serializers.Serializer):
    observer = ObserverSerializer()
    obj = CelestialObjectSerializer()
    dt = serializers.DateTimeField(required=False, default=timezone.now)


class ObserveManySerializer(serializers.Serializer):
    observer = ObserverSerializer()
    objects = CelestialObjectSerializer(many=True)
    dt = serializers.DateTimeField(required=False, default=timezone.now)


class ObservationContextSerializer(serializers.Serializer):
    observer = ObserverSerializer()
    dt = serializers.DateTimeField()
    jd = serializers.FloatField()
    gmst = serializers.FloatField()
    lst = serializers.FloatField()


class CelestialObjectPositionSerializer(serializers.Serializer):
    obj = CelestialObjectSerializer()
    ha = serializers.FloatField()
    alt = serializers.FloatField()
    az = serializers.FloatField()


class ObservationSerializer(serializers.Serializer):
    context = ObservationContextSerializer()
    positions = CelestialObjectPositionSerializer(many=True)
