from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import PermissionDenied
from rest_framework.response import Response

from .serializers import UserSerializer


class AccountView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        if self.kwargs['pk'] != request.user.id:
            raise PermissionDenied
        self.destroy(request, *args, **kwargs)
        return Response(({"message:": "User removed"}), status=status.HTTP_200_OK)
