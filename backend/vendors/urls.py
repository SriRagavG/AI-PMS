# backend/vendors/urls.py (Added AI scoring endpoint)
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet, VendorAIScoreView  # New view

router = DefaultRouter()
router.register(r'', VendorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/ai-score/', VendorAIScoreView.as_view()),  # New: Placeholder for AI scoring
]