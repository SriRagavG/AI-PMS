from django.contrib import admin
from .models import InventoryItem, InventoryCategory
# Register your models here.
admin.site.register(InventoryItem)
admin.site.register(InventoryCategory)
