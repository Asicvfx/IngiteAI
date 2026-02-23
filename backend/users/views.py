import requests as http_requests
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Business
from .serializers import BusinessSerializer
from django.conf import settings
from django.http import QueryDict


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
                token_response = http_requests.post(token_url, data=token_data, timeout=10)
                token_json = token_response.json()

                if 'error' in token_json:
                    return Response(
                        {'error': f"Google token exchange failed: {token_json.get('error_description', token_json['error'])}"},
                        status=status.HTTP_400_BAD_REQUEST
                    )

                access_token = token_json.get('access_token')
                if not access_token:
                    return Response(
                        {'error': 'No access_token received from Google'},
                        status=status.HTTP_400_BAD_REQUEST
                    )

                # Create a mutable QueryDict with the access_token for dj-rest-auth
                mutable_data = QueryDict(mutable=True)
                mutable_data['access_token'] = access_token
                request._request.POST = mutable_data
                # Also set it on the DRF request
                request._data = {'access_token': access_token}
                request._full_data = {'access_token': access_token}

            except http_requests.RequestException as e:
                return Response(
                    {'error': f'Failed to contact Google: {str(e)}'},
                    status=status.HTTP_502_BAD_GATEWAY
                )
            except Exception as e:
                return Response(
                    {'error': f'Internal error during Google auth: {str(e)}'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        # Let dj-rest-auth handle the actual login with access_token
        try:
            return super().post(request, *args, **kwargs)
        except Exception as e:
            return Response(
                {'error': f'Login processing failed: {str(e)}'},
                status=status.HTTP_400_BAD_REQUEST
            )


class BusinessViewSet(viewsets.ModelViewSet):
    serializer_class = BusinessSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Business.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
