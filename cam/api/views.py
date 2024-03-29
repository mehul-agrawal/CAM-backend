# File created at 2024-03-29 16:14:49 UTCfrom rest_framework import viewsets

from rest_framework import viewsets, status, filters , permissions
from cam import models
from cam.api import serializers

class AssignmentView(viewsets.ModelViewSet):
    queryset = models.Assignment.objects.all()
    serializer_class = serializers.AssignmentSerializer
    http_method_names = ["post", "get", "patch"]
    pagination_class = None
    permission_classes = [permissions.AllowAny]

class MarksView(viewsets.ModelViewSet):
    queryset = models.Marks.objects.all()
    serializer_class = serializers.MarksSerializer
    http_method_names = ["post", "get", "patch"]
    pagination_class = None
    permission_classes = [permissions.AllowAny]