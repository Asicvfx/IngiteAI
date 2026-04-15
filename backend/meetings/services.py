from .models import Meeting
from datetime import datetime, timedelta

class BookingService:
    @staticmethod
    def create_meeting(bot, conversation, customer_name, customer_email, start_time_str):
        """Creates a meeting entry."""
        try:
            if not start_time_str:
                print("Booking skipped: missing start_time_str")
                return None
            start_time = datetime.fromisoformat(start_time_str.replace('Z', '+00:00'))
            end_time = start_time + timedelta(minutes=30)
            
            meeting = Meeting.objects.create(
                bot=bot,
                conversation=conversation,
                customer_name=customer_name,
                customer_email=customer_email,
                start_time=start_time,
                end_time=end_time,
                status='pending'
            )
            return meeting
        except Exception as e:
            print(f"Booking Error: {e}; raw_start_time={start_time_str!r}")
            return None

    @staticmethod
    def get_upcoming_meetings(bot):
        return Meeting.objects.filter(bot=bot, start_time__gte=datetime.now()).order_by('start_time')
