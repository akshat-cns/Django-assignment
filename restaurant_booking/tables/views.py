from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .models import Table
from .serializers import TableSerializer

# Create your views here.

class TableViewSet(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAdminUser]  # Restricts access to admin users only

# Admin credentials : Uname- consultadd1, email- example@gmail.com, token- e5450b34d955aba51cac548a2caf0798c74ed50a