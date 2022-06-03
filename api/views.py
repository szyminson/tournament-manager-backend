"""
TODO module docstring
"""
from venv import create
from django.core.mail import send_mail
from django.db.models import Q
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from api.models import  (Category, Tournament,
                         Tree, Staff, Participant,
                         Club, VerificationCode,
                         Duel
                         )
from api.serializers import (CategorySerializer, ClubSerializer,
                             TournamentSerializer, TreeSerializer,
                             VerificationCodeSerializer, DuelSerializer, ParticipantSerializer
                             )
from api.services import TreeGenerator

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def generate_trees(request):
    categories = Category.objects.all()
    tournament = Tournament.objects.first()

    created_trees = []
    for category in categories:
        # ! only one tree  per category!
        if len(Tree.objects.filter(category = category).all()) >= 1:
            print(f"Tree for category '{category.name}' already exists!")
            continue
        generator = TreeGenerator(category, tournament)
        tree = generator.generate()
        serializer = TreeSerializer(tree)
        created_trees.append(serializer.data)
    return Response(created_trees)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def generate_tree(request):
    category = Category.objects.get(id=request.data['category'])
    # ! only one tree  per category!
    if len(Tree.objects.filter(category = category).all()) >= 1:
        return Response({"msg": f"Tree for category '{category.name}' already exists!"})

    tournament = Tournament.objects.first()

    generator = TreeGenerator(category, tournament)
    tree = generator.generate()
    serializer = TreeSerializer(tree)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_tree_by_category(request, category_id, format=None):
    """
    TODO get tree based on given category id.
    """
    choosen_category = Category.objects.get(id=category_id)
    tree = Tree.objects.filter(category = choosen_category).first()
    serializer = TreeSerializer(tree)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def verify_code(request):
    verification_code = VerificationCode.objects.filter(
        code=request.data['code']).first()
    serializer = VerificationCodeSerializer(verification_code)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def me(request):
    user = request.user
    try:
        staff = user.staff
    except Staff.DoesNotExist:
        staff = Staff(user=user)
        staff.save()
        pass
    return Response(
        {
            'id': user.id,
            'name': user.username,
            'email': user.email,
            'type': staff.type
        })

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def emailtest(request):
    """
    Test endpoint for emails
    """
    send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )
    return Response({'message': 'Test email sent.'})

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_codes_capacity(request):
    """
    Get verification codes capacity
    """
    # * get all verification codes
    verification_codes = VerificationCode.objects.all()

    codes_capacity = []

    # * for each verification code - find number of signed participants
    for verficiation_code in verification_codes:
        signed_participants = len(Participant.objects.filter(
            verification_code_id = verficiation_code.id).all())
        club_name = verficiation_code.club.name
        codes_capacity.append({
            "id": verficiation_code.id,
            "club": club_name,
            "verification_code": verficiation_code.code,
            "signed_participants": signed_participants,
            "participants_limit": verficiation_code.participants_limit
        })
    return Response(codes_capacity)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def set_duel_winner(request, participant_id, format=None):
    # find all duels (duplicates) with participant id and update winner
    duels = Duel.objects.filter(Q(participant_one = participant_id) | Q(participant_two = participant_id), winner = None).all()
    winner_participant = Participant.objects.get(id=participant_id)

    if not duels:
        return Response({"msg": f"Participant {winner_participant.first_name} {winner_participant.last_name} CANNOT be move forward!"})

    # normally this loop wouldnt be needed but I have a lot of duplicate duels in my DB
    for duel in duels:
        # * update current duel winner
        duel.winner = winner_participant
        duel.save()
        if duel.parent_duel: # ! tree root is not a duel so check this condition
            parent_duel = Duel.objects.get(id=duel.parent_duel.id)
            # * update parent duel participant
            if parent_duel.participant_one == None:
                parent_duel.participant_one = winner_participant
            elif parent_duel.participant_two == None:
                parent_duel.participant_two = winner_participant
            parent_duel.save()

    return Response({"msg": f"Participant {winner_participant.first_name} {winner_participant.last_name} has been moved forward!"})

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def remove_duel_winner(request, participant_id, format=None):
    # TODO
    pass

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def clear_all_winners(request, participant_id, format=None):
    # TODO
    pass


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def send_verification_code(request):
    """
    TODO docstring
    """
    tournament = Tournament.objects.get(id=1)
    club_id = request.data['club_id']
    print(f"Club id {club_id}")
    club = Club.objects.get(pk=club_id)
    print(f"Club {club}")
    participants_limit = request.data['participants_limit']
    verification_code = VerificationCode(
        participants_limit = participants_limit, club = club)
    verification_code.save()

    subject = f"Invitation for {tournament.name} - {club.name}"
    content = (
     f"Dear {club.ceo}, \n\n  here is your verification code '{verification_code.code}'." +
     f" You can add up to {verification_code.participants_limit} participants!"
     f"\n\nBest Regards,\nOrganizers"
     )

    send_mail(
        subject,
        content,
        tournament.email,
        [club.email],
        fail_silently=False,
    )
    return Response({'message': f'Email for {club.name} has been sent.'})



class ParticipantList(APIView):
    """
    List all Participants, or create a new Participant.
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        """
        TODO docstring
        """
        participants = Participant.objects.all()
        serializer = ParticipantSerializer(participants, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        TODO docstring
        """
        serializer = ParticipantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class ParticipantDetail(APIView):
    """
    TODO docstring
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk, format=None):
        """
        TODO docstring
        """
        participant = Participant.objects.get(id=pk)
        serializer = ParticipantSerializer(participant)
        return Response(serializer.data)


class ClubList(APIView):
    """
    List all Clubs, or create a new Club.
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        """
        TODO docstring
        """
        clubs = Club.objects.all()
        serializer = ClubSerializer(clubs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        TODO docstring
        """
        serializer = ClubSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class ClubDetail(APIView):
    """
    TODO docstring
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk, format=None):
        """
        TODO docstring
        """
        club = Club.objects.get(id=pk)
        serializer = ClubSerializer(club)
        return Response(serializer.data)


class VerificationCodeList(APIView):
    """
    List all Verification Codes, or create a new Verification Code.
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        """
        TODO docstring
        """
        verification_code = VerificationCode.objects.all()
        serializer = VerificationCodeSerializer(verification_code, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        TODO docstring
        """
        serializer = VerificationCodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class VerificationCodeDetail(APIView):
    """
    TODO docstring
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk, format=None):
        """
        TODO docstring
        """
        duel = VerificationCode.objects.get(id=pk)
        serializer = VerificationCodeSerializer(duel)
        return Response(serializer.data)


class DuelList(APIView):
    """
    List all Duels, or create a new Duel.
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        """
        TODO docstring
        """
        duels = Duel.objects.all()
        serializer = DuelSerializer(duels, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        TODO docstring
        """
        serializer = DuelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class DuelDetail(APIView):
    """
    TODO docstring
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk, format=None):
        """
        TODO docstring
        """
        duel = Duel.objects.get(id=pk)
        serializer = DuelSerializer(duel)
        return Response(serializer.data)

    def patch(self, request, pk):
        duel = Duel.objects.get(id=pk)
        serializer = DuelSerializer(duel, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class TournamentList(APIView):
    """
    TODO docstring
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        """
        TODO docstring
        """
        tournaments = Tournament.objects.all()
        serializer = TournamentSerializer(tournaments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        TODO docstring
        """
        serializer = TournamentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class TournamentDetail(APIView):
    """
    TODO docstring
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk, format=None):
        """
        TODO docstring
        """
        tournament = Tournament.objects.get(id=pk)
        serializer = TournamentSerializer(tournament)
        return Response(serializer.data)


class CategoryList(APIView):
    """
    TODO docstring
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        """
        TODO docstring
        """
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        TODO docstring
        """
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    """
    TODO docstring
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk, format=None):
        """
        TODO docstring
        """
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class TreeList(APIView):
    """
    TODO docstring
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        """
        TODO docstring
        """
        trees = Tree.objects.all()
        serializer = TreeSerializer(trees, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        TODO docstring
        """
        serializer = TreeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class TreeDetail(APIView):
    """
    TODO docstring
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk, format=None):
        """
        TODO docstring
        """
        tree = Tree.objects.get(id=pk)
        serializer = TreeSerializer(tree)
        return Response(serializer.data)
