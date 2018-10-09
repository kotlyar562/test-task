from rest_framework import serializers
from . models import Country, City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('pk', 'title', 'desc')

class CountrySerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, required=False)
    class Meta:
        model = Country
        fields = ('pk', 'title', 'text', 'cities')