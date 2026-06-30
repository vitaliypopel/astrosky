from rest_framework import serializers

from .models import Catalog, Constellation, Star


class CatalogSerializer(serializers.ModelSerializer):
    stars_count = serializers.IntegerField(read_only=True)
    named_stars_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Catalog
        fields = '__all__'


class ConstellationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Constellation
        fields = '__all__'


class StarSerializer(serializers.ModelSerializer):
    names = serializers.SerializerMethodField()
    catalog = CatalogSerializer(read_only=True)
    constellation = ConstellationSerializer(read_only=True)

    class Meta:
        model = Star
        fields = '__all__'

    def get_names(self, star: Star) -> list[str]:
        return star.get_names()
