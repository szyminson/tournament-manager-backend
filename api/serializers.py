"""
Model serializer aggregating module
"""
from rest_framework import serializers
from api.models import Category, Club, Tournament, Tree, VerificationCode, Duel, User, Participant


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
    
    def to_representation(self, instance):
        self.fields['club'] =  ClubSerializer(read_only=True)
        return super( VerificationCodeSerializer, self).to_representation(instance)

class DuelSerializer(serializers.ModelSerializer):
    """
    Duel model serializer
    """
    class Meta:
        model = Duel
        fields = ('participant_one', 'participant_two', 'parent_duel',
                  'winner', 'score_description')

class UserSerializer(serializers.ModelSerializer):
    """
    User model serializer
    """
    class Meta:
        model = User
        fields = ('username', 'email', 'hashed_password', 'user_type')

class TournamentSerializer(serializers.ModelSerializer):
    """
    Tournament model serializer
    """
    class Meta:
        model = Tournament
        fields = ('time', 'date', 'location')

class CategorySerializer(serializers.ModelSerializer):
    """
    Category model serializer
    """
    class Meta:
        model = Category
        fields = ('category_name', 'description')


class TreeSerializer(serializers.ModelSerializer):
    """
    VerificationCode model serializer
    """
    class Meta:
        model = Tree
        fields = ('category', 'root_duel', 'tournament')

class ParticipantSerializer(serializers.ModelSerializer):
    """
    VerificationCode model serializer
    """
    class Meta:
        model = Participant
        fields = ('first_name', 'last_name', 'gender', 'date_of_birth', 'club', 'verification_code')