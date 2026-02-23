from rest_framework import serializers
from .models import Business, User


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username', 'email', 'first_name', 'last_name', 'is_superuser']
        read_only_fields = ['pk', 'email', 'is_superuser']


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ['id', 'user', 'name', 'website', 'industry', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']

    def create(self, validated_data):
        user = self.context['request'].user
        business, created = Business.objects.update_or_create(user=user, defaults=validated_data)
        return business
