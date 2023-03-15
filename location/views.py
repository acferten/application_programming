from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.exceptions import ValidationError

from animal.models import Animal
from .models import Location
from .serializers import LocationSerializer


class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    model = Location
    serializer_class = LocationSerializer

    def get(self, request, *args, **kwargs):
        if int(self.kwargs['pk']) <= 0:
            raise ValidationError
        return self.retrieve(request, *args, **kwargs)


class AnimalLocationsView(generics.ListAPIView):
    model = Location
    serializer_class = LocationSerializer

    def get_queryset(self, **kwargs):
        return get_object_or_404(Animal, id=self.kwargs['pk']).visitedLocations.all()
