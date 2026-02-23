from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

User = get_user_model()


class AdminStatsView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        now = timezone.now()
        today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
        week_ago = now - timedelta(days=7)

        total_users = User.objects.count()
        new_today = User.objects.filter(date_joined__gte=today_start).count()
        new_this_week = User.objects.filter(date_joined__gte=week_ago).count()

        # User list
        users = User.objects.order_by('-date_joined').values(
            'id', 'username', 'email', 'date_joined', 'last_login', 'is_active', 'is_superuser'
        )

        user_list = []
        for u in users:
            user_list.append({
                'id': u['id'],
                'username': u['username'],
                'email': u['email'],
                'date_joined': u['date_joined'].isoformat() if u['date_joined'] else None,
                'last_login': u['last_login'].isoformat() if u['last_login'] else None,
                'is_active': u['is_active'],
                'is_superuser': u['is_superuser'],
            })

        return Response({
            'total_users': total_users,
            'new_today': new_today,
            'new_this_week': new_this_week,
            'users': user_list,
        })
