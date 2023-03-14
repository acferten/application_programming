from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Animal
from .serializers import AnimalSerializer


class AnimalDetailView(generics.RetrieveUpdateDestroyAPIView):
    model = Animal
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [IsAuthenticated]
