from rest_framework import serializers
from .models import Report 

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'title', 'description', 'generated_by', 'data', 'created_at', 'is_active']
        read_only_fields = ['id', 'created_at']
