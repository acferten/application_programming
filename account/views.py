from rest_framework import generics, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import authentication_classes
from django.core.exceptions import PermissionDenied
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import AdvUser
from .serializers import AccountSerializer, CreateAccountSerializer


class AccountView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdvUser.objects.all()
    serializer_class = AccountSerializer

    def get(self, request, *args, **kwargs):
        if int(self.kwargs['pk']) <= 0:
            raise ValidationError
        return self.retrieve(request, *args, **kwargs)

    @authentication_classes([BasicAuthentication])
    def delete(self, request, *args, **kwargs):
        if self.kwargs['pk'] != request.user.id:
            raise PermissionDenied
        self.destroy(request, *args, **kwargs)
        return Response(({"message:": "User removed"}), status=status.HTTP_200_OK)


class CreateAccountView(generics.CreateAPIView):
    queryset = AdvUser.objects.all()
    serializer_class = CreateAccountSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response({"message": 'User created', "status:": status.HTTP_201_CREATED},
                        status=status.HTTP_201_CREATED, headers=headers)


class SearchAccountView(generics.ListAPIView):
    queryset = AdvUser.objects.all()
    serializer_class = AccountSerializer
    filterset_fields = ['id', 'first_name', 'last_name', 'email']
