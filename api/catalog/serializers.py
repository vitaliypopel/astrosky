from rest_framework import serializers

from .models import Catalog, Star


class CatalogSerializer(serializers.ModelSerializer):
    stars_count = serializers.IntegerField(read_only=True)
    named_stars_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Catalog
        fields = (
            'id',
            'name',
            'code',
            'description',
            'stars_count',
            'named_stars_count',
            'created_at',
            'updated_at',
        )


class StarSerializer(serializers.ModelSerializer):
    catalog = CatalogSerializer()

    class Meta:
        model = Star
        fields = '__all__'
