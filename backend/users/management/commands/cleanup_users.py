import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


ALLOWED_DOMAINS = [
    'gmail.com', 'googlemail.com',
    'mail.ru', 'inbox.ru', 'list.ru', 'bk.ru',
    'yandex.ru', 'yandex.kz', 'yandex.com', 'ya.ru',
    'outlook.com', 'hotmail.com', 'live.com', 'msn.com',
    'icloud.com', 'me.com', 'mac.com',
    'yahoo.com', 'yahoo.co.uk',
    'protonmail.com', 'proton.me',
    'zoho.com', 'aol.com',
]


class Command(BaseCommand):
    help = 'Deletes users with fake/non-existent email domains (keeps superusers)'

    def handle(self, *args, **options):
        User = get_user_model()
        fake_users = []

        for user in User.objects.filter(is_superuser=False):
            if not user.email or '@' not in user.email:
                fake_users.append(user)
                continue
            domain = user.email.split('@')[1].lower()
            if domain not in ALLOWED_DOMAINS:
                fake_users.append(user)

        if not fake_users:
            self.stdout.write(self.style.SUCCESS('No fake accounts found.'))
            return

        self.stdout.write(f'Found {len(fake_users)} accounts with fake email domains:')
        for u in fake_users:
            self.stdout.write(f'  - {u.username} ({u.email})')

        for u in fake_users:
            u.delete()

        self.stdout.write(self.style.SUCCESS(f'Deleted {len(fake_users)} fake accounts.'))
