from rest_framework import serializers

from .models import Constellation, Star


class ConstellationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Constellation
        fields = '__all__'


class StarSerializer(serializers.ModelSerializer):
    names = serializers.SerializerMethodField()
    constellation = ConstellationSerializer(read_only=True)

    class Meta:
        model = Star
        fields = '__all__'

    def get_names(self, star: Star) -> list[str]:
        return star.get_names()
