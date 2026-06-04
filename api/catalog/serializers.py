from rest_framework import serializers

from .models import Catalog, Star


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = '__all__'


class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = '__all__'
