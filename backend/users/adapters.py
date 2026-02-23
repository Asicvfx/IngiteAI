from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model


ALLOWED_EMAIL_DOMAINS = [
    'gmail.com', 'googlemail.com',
    'mail.ru', 'inbox.ru', 'list.ru', 'bk.ru',
    'yandex.ru', 'yandex.kz', 'yandex.com', 'ya.ru',
    'outlook.com', 'hotmail.com', 'live.com', 'msn.com',
    'icloud.com', 'me.com', 'mac.com',
    'yahoo.com', 'yahoo.co.uk',
    'protonmail.com', 'proton.me',
    'zoho.com', 'aol.com',
]


class CustomAccountAdapter(DefaultAccountAdapter):
    """Blocks registration with fake email domains on the backend."""

    def clean_email(self, email):
        email = super().clean_email(email)
        if email and '@' in email:
            domain = email.split('@')[1].lower()
            if domain not in ALLOWED_EMAIL_DOMAINS:
                from django.core.exceptions import ValidationError
                raise ValidationError(
                    f'Registration with @{domain} is not allowed. '
                    'Use Gmail, Mail.ru, Yandex, Outlook, or another trusted provider.'
                )
        return email


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    """Auto-connects Google account to existing user with matching email."""

    def pre_social_login(self, request, sociallogin):
        """
        If a user with this email already exists (e.g. superuser admin with
        asyl042007@gmail.com), automatically link the social account to that
        existing user instead of creating a duplicate or throwing an error.
        """
        if sociallogin.is_existing:
            return

        email = sociallogin.account.extra_data.get('email', '').lower()
        if not email:
            return

        User = get_user_model()
        try:
            existing_user = User.objects.get(email__iexact=email)
            sociallogin.connect(request, existing_user)
        except User.DoesNotExist:
            pass
