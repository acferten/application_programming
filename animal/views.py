from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Animal
from .serializers import AnimalSerializer


class AnimalDetailView(generics.RetrieveUpdateDestroyAPIView):
    model = Animal
    serializer_class = AnimalSerializer
    permission_classes = [IsAuthenticated]
