from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from . models import Country, City
from . serializers import CountrySerializer, CitySerializer


class CountriesView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        country_pk = request.data.get('country_pk', 0)
        country = get_object_or_404(Country, pk=country_pk)
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(country=country)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, *args, **kwargs):
        city_pk = request.data.get('pk', 0)
        city = get_object_or_404(City, pk=city_pk)
        serializer = CitySerializer(instance=city, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        city_pk = request.data.get('city_pk', 0)
        city = get_object_or_404(City, pk=city_pk)
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)