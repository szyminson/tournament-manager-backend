"""
Model serializer aggregating module
"""
from rest_framework import serializers
from api.models import Club, VerificationCode


class ClubSerializer(serializers.ModelSerializer):
    """
    Club model serializer
    """
    class Meta:
        model = Club
        fields = ('club_name', 'club_ceo')

class VerificationCodeSerializer(serializers.ModelSerializer):
    """
    VerificationCode model serializer
    """
    class Meta:
        model = VerificationCode
        fields = ('code', 'participants_limit', 'club')
