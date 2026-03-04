# backend/inventory/urls.py (Added category list for AI)
from django.urls import path
from .views import InventoryItemListView, InventoryCategoryListView  # New view

urlpatterns = [
    path('items/', InventoryItemListView.as_view()),
    path('categories/', InventoryCategoryListView.as_view()),  # New for AI category matching
]