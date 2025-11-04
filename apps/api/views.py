from rest_framework import generics
from apps.core.models import Item
from .serializers import ItemSerializer
from django.views.generic import TemplateView

class ItemListCreateView(generics.ListCreateAPIView):
    """
    GET: list items
    POST: create new item
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: retrieve item
    PUT/PATCH: update item
    DELETE: delete item
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class APIFrontendView(TemplateView):
    """
    Frontend page for the API endpoints at /api/items/
    """
    template_name = "api/items.html"