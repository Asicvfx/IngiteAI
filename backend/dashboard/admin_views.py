from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

User = get_user_model()


class HeartbeatView(APIView):
    """Receives ping from frontend every 60 sec to track online status."""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        now = timezone.now()

        # If no session or last_seen was > 5 min ago, start new session
        if not user.session_start or not user.last_seen or (now - user.last_seen).total_seconds() > 300:
            user.session_start = now

        user.last_seen = now
        user.save(update_fields=['last_seen', 'session_start'])

        return Response({'status': 'ok'})


class AdminStatsView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        now = timezone.now()
        today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
        week_ago = now - timedelta(days=7)

        total_users = User.objects.count()
        new_today = User.objects.filter(date_joined__gte=today_start).count()
        new_this_week = User.objects.filter(date_joined__gte=week_ago).count()

        # Count online users (last_seen within 2 min)
        online_cutoff = now - timedelta(minutes=2)
        online_count = User.objects.filter(last_seen__gte=online_cutoff).count()

        users = User.objects.order_by('-date_joined').values(
            'id', 'username', 'email', 'date_joined', 'last_login',
            'is_active', 'is_superuser', 'last_seen', 'session_start'
        )

        user_list = []
        for u in users:
            # Calculate online status and session duration
            is_online = False
            session_minutes = 0
            if u['last_seen'] and (now - u['last_seen']).total_seconds() < 120:
                is_online = True
                if u['session_start']:
                    session_minutes = int((now - u['session_start']).total_seconds() / 60)

            user_list.append({
                'id': u['id'],
                'username': u['username'],
                'email': u['email'],
                'date_joined': u['date_joined'].isoformat() if u['date_joined'] else None,
                'last_login': u['last_login'].isoformat() if u['last_login'] else None,
                'is_active': u['is_active'],
                'is_superuser': u['is_superuser'],
                'is_online': is_online,
                'session_minutes': session_minutes,
                'last_seen': u['last_seen'].isoformat() if u['last_seen'] else None,
            })

        return Response({
            'total_users': total_users,
            'new_today': new_today,
            'new_this_week': new_this_week,
            'online_count': online_count,
            'users': user_list,
        })


class AdminDeleteUserView(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

        if user.is_superuser:
            return Response({'error': 'Cannot delete a superuser'}, status=403)

        username = user.username
        user.delete()
        return Response({'message': f'User "{username}" deleted successfully'})
