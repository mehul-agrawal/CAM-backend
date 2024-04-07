
from rest_framework import viewsets, status, filters , permissions
from cam import models
from cam.api import serializers
from django_filters.rest_framework import DjangoFilterBackend

class AssignmentView(viewsets.ModelViewSet):
    queryset = models.Assignment.objects.all()
    serializer_class = serializers.AssignmentSerializer
    http_method_names = ["post", "get", "patch"]
    pagination_class = None
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["subject"]

class MarksView(viewsets.ModelViewSet):
    queryset = models.Marks.objects.all()
    serializer_class = serializers.MarksSerializer
    http_method_names = ["post", "get", "patch"]
    pagination_class = None
    permission_classes = [permissions.AllowAny]