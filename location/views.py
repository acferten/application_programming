from rest_framework import generics
from rest_framework.exceptions import ValidationError

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
