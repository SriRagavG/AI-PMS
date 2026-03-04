# backend/inventory/models.py (Added category for AI suggestions matching)
from django.db import models

class InventoryCategory(models.Model):  # New model for categories (AI-ready for vendor matching)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(InventoryCategory, on_delete=models.SET_NULL, null=True, blank=True)  # Updated to FK for AI categorization
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name