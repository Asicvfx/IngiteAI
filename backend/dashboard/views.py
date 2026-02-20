from rest_framework.views import APIView
from rest_framework.response import Response
from chats.models import Conversation, Message
from django.db.models import Count
from rest_framework.permissions import IsAuthenticated

class AnalyticsView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # 1. Lead types distribution
        leads_data = Conversation.objects.filter(bot__user=request.user).values('lead_type').annotate(count=Count('id'))
        
        # 2. Total platform metrics
        total_messages = Message.objects.filter(conversation__bot__user=request.user).count()
        total_conversations = Conversation.objects.filter(bot__user=request.user).count()
        hot_leads = Conversation.objects.filter(bot__user=request.user, lead_type='hot').count()
        needs_human = Conversation.objects.filter(bot__user=request.user, needs_human=True).count()
        
        # 3. Simple sentiment placeholder (could be expanded with real AI scoring)
        # For now, let's derive it from lead types: hot = positive, cold = neutral
        sentiment = {
            "positive": hot_leads,
            "neutral": Conversation.objects.filter(bot__user=request.user, lead_type='warm').count(),
            "needs_attention": needs_human
        }
        
        return Response({
            "leads": leads_data,
            "metrics": {
                "total_messages": total_messages,
                "total_conversations": total_conversations,
                "hot_leads": hot_leads,
                "needs_human": needs_human
            },
            "sentiment": sentiment
        })
