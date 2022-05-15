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
        fields = ('id', 'name', 'ceo', 'email')

class VerificationCodeSerializer(serializers.ModelSerializer):
    """
    VerificationCode model serializer
    """
    class Meta:
        model = VerificationCode
        fields = ('id','code', 'participants_limit', 'club')

    def to_representation(self, instance):
        self.fields['club'] =  ClubSerializer(read_only=True)
        return super( VerificationCodeSerializer, self).to_representation(instance)

class DuelSerializer(serializers.ModelSerializer):
    """
    Duel model serializer
    """
    class Meta:
        model = Duel
        fields = ('id','participant_one', 'participant_two', 'parent_duel',
                  'winner', 'score_description')

class UserSerializer(serializers.ModelSerializer):
    """
    User model serializer
    """
    class Meta:
        model = User
        fields = ('id','username', 'email', 'hashed_password', 'user_type')

class TournamentSerializer(serializers.ModelSerializer):
    """
    Tournament model serializer
    """
    class Meta:
        model = Tournament
        fields = ('id','name', 'start_date', 'end_date', 'location', 'phone_number', 'email')

class CategorySerializer(serializers.ModelSerializer):
    """
    Category model serializer
    """
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class TreeSerializer(serializers.ModelSerializer):
    """
    VerificationCode model serializer
    """
    class Meta:
        model = Tree
        fields = ('id', 'category', 'root_duel', 'tournament')

class ParticipantSerializer(serializers.ModelSerializer):
    """
    VerificationCode model serializer
    """
    class Meta:
        model = Participant
        fields = ('id', 'first_name', 'last_name', 'gender', 'date_of_birth', 'club', 'verification_code', 'category')

    def to_representation(self, instance):
        self.fields['club'] =  ClubSerializer(read_only=True)
        self.fields['verification_code'] = VerificationCodeSerializer(read_only=True)
        self.fields['category'] = CategorySerializer(read_only=True)
        return super( ParticipantSerializer, self).to_representation(instance)

