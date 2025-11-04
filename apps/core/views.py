from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer
from django.views.generic import TemplateView

class ItemViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Item model providing standard CRUD operations.
    - queryset: all items ordered by created_at (if present)
    - serializer_class: ItemSerializer
    """
    queryset = Item.objects.all().order_by('-id')
    serializer_class = ItemSerializer
    lookup_field = 'pk'

    def list(self, request):
        items = self.get_queryset()
        serializer = self.get_serializer(items, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        item = self.get_object()
        serializer = self.get_serializer(item, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        item = self.get_object()
        serializer = self.get_serializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        item = self.get_object()
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ItemFrontendView(TemplateView):
    """
    Basic frontend for core Item endpoints.
    Renders templates/core/items.html which calls /api/core/items/ via fetch.
    """
    template_name = "core/items.html"