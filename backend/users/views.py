import requests
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Business
from .serializers import BusinessSerializer
from django.conf import settings


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

    def post(self, request, *args, **kwargs):
        # Authorization Code flow: exchange code for access_token first
        code = request.data.get('code')
        redirect_uri = request.data.get('redirect_uri')

        if code and redirect_uri:
            # Exchange authorization code for access token via Google
            token_url = 'https://oauth2.googleapis.com/token'
            google_config = settings.SOCIALACCOUNT_PROVIDERS.get('google', {}).get('APP', {})
            
            token_data = {
                'code': code,
                'client_id': google_config.get('client_id', ''),
                'client_secret': google_config.get('secret', ''),
                'redirect_uri': redirect_uri,
                'grant_type': 'authorization_code',
            }

            try:
                token_response = requests.post(token_url, data=token_data, timeout=10)
                token_json = token_response.json()

                if 'error' in token_json:
                    return Response(
                        {'error': f"Google token exchange failed: {token_json.get('error_description', token_json['error'])}"},
                        status=status.HTTP_400_BAD_REQUEST
                    )

                # Replace the code with the access_token for dj-rest-auth
                access_token = token_json.get('access_token')
                if access_token:
                    request._full_data = {'access_token': access_token}
                else:
                    return Response(
                        {'error': 'No access_token received from Google'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            except requests.RequestException as e:
                return Response(
                    {'error': f'Failed to contact Google: {str(e)}'},
                    status=status.HTTP_502_BAD_GATEWAY
                )

        # Let dj-rest-auth handle the actual login with access_token
        return super().post(request, *args, **kwargs)


class BusinessViewSet(viewsets.ModelViewSet):
    serializer_class = BusinessSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Business.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
