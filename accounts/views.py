from .models import Account
from rest_framework import viewsets, permissions
from .serializers import AccountSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework import status

# AccountViewSet


class AccountViewSet(viewsets.ModelViewSet):

    serializer_class = AccountSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = Account.objects.all()

        # Query tags allowed
        id = self.request.query_params.get('id')
        email = self.request.query_params.get('email')
        programme = self.request.query_params.get('programme')
        role = self.request.query_params.get('role')
        school = self.request.query_params.get('school')

        if id is not None:
            queryset = queryset.filter(id=id)
        if email is not None:
            queryset = queryset.filter(email=email)
        if programme is not None:
            queryset = queryset.filter(programme=programme)
        if role is not None:
            queryset = queryset.filter(role=role)
        if school is not None:
            queryset = queryset.filter(school=school)

        return queryset
