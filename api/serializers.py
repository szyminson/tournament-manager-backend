"""
Model serializer aggregating module
"""
from rest_framework import serializers
from api.models import Club


class ClubSerializer(serializers.ModelSerializer):
    """
    Club model serializer
    """
    class Meta:
        model = Club
        fields = ('club_name', 'club_ceo')
