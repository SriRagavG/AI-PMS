# backend/vendors/admin.py (Added new AI fields to admin)
from django.contrib import admin
from .models import Vendor, DeliveryHistory

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'reliability_score', 'ai_risk_score')  # New AI field in list
    readonly_fields = ('ai_explanation',)  # Display AI explanation

@admin.register(DeliveryHistory)
class DeliveryHistoryAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'delivered_on', 'was_on_time')