from rest_framework import generics
from rest_framework.exceptions import ValidationError

from .models import Animal
from .serializers import AnimalSerializer


class AnimalDetailView(generics.RetrieveUpdateDestroyAPIView):
    model = Animal
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def get(self, request, *args, **kwargs):
        if int(self.kwargs['pk']) <= 0:
            raise ValidationError
        return self.retrieve(request, *args, **kwargs)
