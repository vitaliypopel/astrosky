from django.utils import timezone
from rest_framework import serializers


class ObserverSerializer(serializers.Serializer):
    lat = serializers.FloatField()
    lon = serializers.FloatField()


class StellarObjectSerializer(serializers.Serializer):
    ra = serializers.FloatField()
    dec = serializers.FloatField()


class ObserveSerializer(serializers.Serializer):
    observer = ObserverSerializer()
    obj = StellarObjectSerializer()
    dt = serializers.DateTimeField(required=False, default=timezone.now)


class ObserveManySerializer(serializers.Serializer):
    observer = ObserverSerializer()
    objects = StellarObjectSerializer(many=True)
    dt = serializers.DateTimeField(required=False, default=timezone.now)


class ObservationContextSerializer(serializers.Serializer):
    observer = ObserverSerializer()
    dt = serializers.DateTimeField()
    jd = serializers.FloatField()
    gmst = serializers.FloatField()
    lst = serializers.FloatField()


class StellarPositionSerializer(serializers.Serializer):
    obj = StellarObjectSerializer()
    ha = serializers.FloatField()
    alt = serializers.FloatField()
    az = serializers.FloatField()


class ObservationSerializer(serializers.Serializer):
    context = ObservationContextSerializer()
    positions = StellarPositionSerializer(many=True)
