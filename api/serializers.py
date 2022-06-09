"""
Model serializer aggregating module
"""
from rest_framework import serializers
from api.models import Category, Club, Tournament, Tree, VerificationCode, Duel, Participant


class ClubSerializer(serializers.ModelSerializer):
    """
    Club model serializer
    """
    class Meta:
        model = Club
        fields = ('id', 'name', 'ceo', 'email')

    # Data validation
    def validate_name(self, value):
        if len(value) == 0:
            raise serializers.ValidationError('Name of the club cannot be empty')
        if len(value) > 45:
            raise serializers.ValidationError('Name of the club is too long')
        return value

    def validate_ceo(self, value):
        if len(value) == 0:
            raise serializers.ValidationError('Name of CEO of the club cannot be empty')
        if len(value) > 45:
            raise serializers.ValidationError('Name of CEO of the club is too long')
        return value

    def validate_email(self, value):
        if len(value) == 0:
            raise serializers.ValidationError('E-mail of the club cannot be empty')
        if len(value) > 45:
            raise serializers.ValidationError('E-mail of the club is too long')
        return value

class VerificationCodeSerializer(serializers.ModelSerializer):
    """
    VerificationCode model serializer
    """
    class Meta:
        model = VerificationCode
        fields = ('id', 'code', 'participants_limit', 'club')

    def to_representation(self, instance):
        self.fields['club'] = ClubSerializer(read_only=True)
        return super(VerificationCodeSerializer, self).to_representation(instance)

class DuelSerializer(serializers.ModelSerializer):
    """
    Duel model serializer
    """
    class Meta:
        model = Duel
        fields = ('id', 'participant_one', 'participant_two', 'parent_duel',
                  'winner', 'score_description')


class TournamentSerializer(serializers.ModelSerializer):
    """
    Tournament model serializer
    """
    class Meta:
        model = Tournament
        fields = ('id', 'name', 'start_date', 'end_date',
                  'location', 'phone_number', 'email')

    # Data validation
    def validate_name(self, value):
        if len(value) == 0:
            raise serializers.ValidationError('Name of tournament cannot be empty')
        if len(value) > 45:
            raise serializers.ValidationError('Name of tournament is too long')
        return value

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError('End date cannot be before start date')
        return data

class CategorySerializer(serializers.ModelSerializer):
    """
    Category model serializer
    """
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')

    # Data validation
    def validate_name(self, value):
        if len(value) == 0:
            raise serializers.ValidationError('Name of category cannot be empty')
        if len(value) > 45:
            raise serializers.ValidationError('Name of category is too long')
        return value

    def validate_description(self, value):
        if len(value) == 0:
            raise serializers.ValidationError('Category description cannot be empty')
        if len(value) > 45:
            raise serializers.ValidationError('Category description is too long')
        return value

class TreeSerializer(serializers.ModelSerializer):
    """
    VerificationCode model serializer
    """
    structure = serializers.SerializerMethodField()

    class Meta:
        model = Tree
        fields = ('id', 'category', 'root_duel', 'tournament', 'structure')

    def get_structure(self, obj):
        root_duel = obj.root_duel
        return self.retrieve_duel_structure(root_duel)

    def retrieve_duel_structure(self, duel):
        child_duels = duel.duel_set.all()
        children = []
        if not child_duels:
            children.append(self.create_node_dict(duel.participant_one, [], duel.id))
            children.append(self.create_node_dict(duel.participant_two, [], duel.id))
        else:
            if len(child_duels) < 2:
                if duel.participant_one:
                    children.append(self.create_node_dict(duel.participant_one, []))
                elif duel.participant_two:
                    children.append(self.create_node_dict(duel.participant_two, []))
            for child in child_duels:
                children.append(self.retrieve_duel_structure(child))
        return self.create_node_dict(duel.winner, children, duel.id)

    def create_node_name(self, participant):
        if not participant:
            return "TBA"
        return f"{participant.first_name} {participant.last_name}"

    def create_node_dict(self, participant, children, duel_id = 0):
        participant_id = 0
        if participant:
            participant_id = participant.id
        return {
            "name": self.create_node_name(participant),
            "duel_id": duel_id,
            "participant_id": participant_id,
            "children": children,
        }

    def to_representation(self, instance):
        self.fields['category'] =  CategorySerializer(read_only=True)
        return super( TreeSerializer, self).to_representation(instance)

class ParticipantSerializer(serializers.ModelSerializer):
    """
    VerificationCode model serializer
    """
    class Meta:
        model = Participant
        fields = ('id', 'first_name', 'last_name', 'gender',
                  'date_of_birth', 'club', 'verification_code', 'category')

    def to_representation(self, instance):
        self.fields['club'] = ClubSerializer(read_only=True)
        self.fields['verification_code'] = VerificationCodeSerializer(
            read_only=True)
        self.fields['category'] = CategorySerializer(read_only=True)
        return super(ParticipantSerializer, self).to_representation(instance)

    # Data validation
    def validate_first_name(self, value):
        if len(value) == 0:
            raise serializers.ValidationError('First name cannot be empty')
        if len(value) > 30:
            raise serializers.ValidationError('First name is too long')
        return value

    def validate_last_name(self, value):
        if len(value) == 0:
            raise serializers.ValidationError('Last name cannot be empty')
        if len(value) > 30:
            raise serializers.ValidationError('Last name is too long')
        return value

    
