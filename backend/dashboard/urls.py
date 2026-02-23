from django.urls import path
from .views import AnalyticsView
from .admin_views import AdminStatsView, AdminDeleteUserView

urlpatterns = [
    path('analytics/', AnalyticsView.as_view(), name='analytics'),
    path('admin-stats/', AdminStatsView.as_view(), name='admin-stats'),
    path('admin-stats/delete-user/<int:user_id>/', AdminDeleteUserView.as_view(), name='admin-delete-user'),
]
