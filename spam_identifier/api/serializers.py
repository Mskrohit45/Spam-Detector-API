from rest_framework import serializers
from .models import User, Contact, SpamFlag

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'phone_number', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class SpamFlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpamFlag
        fields = ['phone_number', 'flagged_count']
