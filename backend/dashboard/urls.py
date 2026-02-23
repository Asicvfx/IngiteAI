from django.urls import path
from .views import AnalyticsView
from .admin_views import AdminStatsView

urlpatterns = [
    path('analytics/', AnalyticsView.as_view(), name='analytics'),
    path('admin-stats/', AdminStatsView.as_view(), name='admin-stats'),
]
