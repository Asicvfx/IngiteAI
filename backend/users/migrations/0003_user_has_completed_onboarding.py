from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_last_seen_user_session_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_completed_onboarding',
            field=models.BooleanField(default=False),
        ),
    ]
