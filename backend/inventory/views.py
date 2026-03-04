# backend/inventory/views.py (Added category list)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import InventoryItem, InventoryCategory
from .serializers import InventoryItemSerializer, InventoryCategorySerializer

class InventoryItemListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        items = InventoryItem.objects.all()
        serializer = InventoryItemSerializer(items, many=True)
        return Response(serializer.data)

class InventoryCategoryListView(APIView):  # New for AI
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        categories = InventoryCategory.objects.all()
        serializer = InventoryCategorySerializer(categories, many=True)
        return Response(serializer.data)