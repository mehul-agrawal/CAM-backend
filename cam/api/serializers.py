# File created at 2024-03-29 16:14:49 UTCfrom rest_framework import serializers

from rest_framework import serializers
from cam.models import Assignment, Marks

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'

class MarksSerializer(serializers.ModelSerializer):
    assignment_name = serializers.SerializerMethodField(read_only=True)
    total_marks = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Marks
        fields = '__all__'

    def get_assignment_name(self, obj):
        return obj.assignment.name
    
    def get_total_marks(self, obj):
        return obj.spo_marks + obj.rpp_marks