from rest_framework import serializers
from apps.core.models import Item # Replace with your actual model

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item  # Replace with your actual model
        fields = '__all__'  # Specify the fields you want to include in the serialization

# Bridge serializer so apps.api can import ItemSerializer
from apps.core.serializers import ItemSerializer
# nothing else needed here; kept to satisfy imports in views
