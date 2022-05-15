"""
TODO module docstring
"""
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from api.models import Category, Staff, Tournament, Tree, Participant, Club, VerificationCode, Duel
from api.serializers import (CategorySerializer, ClubSerializer,
                             TournamentSerializer, TreeSerializer,
                             VerificationCodeSerializer, DuelSerializer, ParticipantSerializer
                             )


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
            return Response(request.data, status=status.HTTP_201_CREATED)
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
