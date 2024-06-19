from rest_framework import viewsets
from rest_framework import serializers
from backend.models import Number
from backend.serializers.NumberSerializer import NumberSerializer

class NumberViewSet(viewsets.ModelViewSet):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer

