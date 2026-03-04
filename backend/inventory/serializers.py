# backend/inventory/serializers.py (Updated for category)
from rest_framework import serializers
from .models import InventoryItem, InventoryCategory

class InventoryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryCategory
        fields = ['id', 'name', 'description']

class InventoryItemSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')  # New for AI use

    class Meta:
        model = InventoryItem
        fields = ['id', 'name', 'category', 'category_name', 'current_stock', 'unit_price']