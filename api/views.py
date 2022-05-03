"""
TODO module docstring
"""
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Category, Tournament, Tree, User, Participant, Club, VerificationCode, Duel
from api.serializers import (CategorySerializer, ClubSerializer,
    TournamentSerializer, TreeSerializer,
    VerificationCodeSerializer, DuelSerializer,
    UserSerializer, ParticipantSerializer
)


## ! Test view. Can be deleted when necessary
#@api_view(['GET'])
#@permission_classes([permissions.AllowAny])
#def createUser(request):
#    user = User(username="workata", email="cos@gmail.com", hashed_password="1234", user_type= User.UserType.ADMINISTRATOR)
#    user.save()
#    return Response(user)

class ParticipantList(APIView):
    """
    List all Participants, or create a new Participant.
    """
    permission_classes=[permissions.AllowAny]

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
        serializer = ParticipantSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

class ParticipantDetail(APIView):
    """
    TODO docstring
    """
    permission_classes=[permissions.AllowAny]

    def get(self, request, pk, format=None):
        """
        TODO docstring
        """
        participant = Participant.objects.get(id = pk)
        serializer = ParticipantSerializer(participant)
        return Response(serializer.data)

class ClubList(APIView):
    """
    List all Clubs, or create a new Club.
    """
    permission_classes=[permissions.AllowAny]

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
        serializer = ClubSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

class ClubDetail(APIView):
    """
    TODO docstring
    """
    permission_classes=[permissions.AllowAny]

    def get(self, request, pk, format=None):
        """
        TODO docstring
        """
        club = Club.objects.get(id = pk)
        serializer = ClubSerializer(club)
        return Response(serializer.data)

class VerificationCodeList(APIView):
    """
    List all Verification Codes, or create a new Verification Code.
    """
    permission_classes=[permissions.AllowAny]

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
        serializer = VerificationCodeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

class VerificationCodeDetail(APIView):
    """
    TODO docstring
    """
    permission_classes=[permissions.AllowAny]

    def get(self, request, pk, format=None):
        """
        TODO docstring
        """
        duel = VerificationCode.objects.get(id = pk)
        serializer = VerificationCodeSerializer(duel)
        return Response(serializer.data)

class DuelList(APIView):
    """
    List all Duels, or create a new Duel.
    """
    permission_classes=[permissions.AllowAny]

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
        serializer = DuelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

class DuelDetail(APIView):
    """
    TODO docstring
    """
    permission_classes=[permissions.AllowAny]

    def get(self, request, pk, format=None):
        """
        TODO docstring
        """
        duel = Duel.objects.get(id = pk)
        serializer = DuelSerializer(duel)
        return Response(serializer.data)

class TournamentList(APIView):
    """
    TODO docstring
    """
    permission_classes=[permissions.AllowAny]

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
        serializer = TournamentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

class TournamentDetail(APIView):
    """
    TODO docstring
    """
    permission_classes=[permissions.AllowAny]

    def get(self, request, pk, format=None):
        """
        TODO docstring
        """
        tournament = Tournament.objects.get(id = pk)
        serializer = TournamentSerializer(tournament)
        return Response(serializer.data)


class CategoryList(APIView):
    """
    TODO docstring
    """
    permission_classes=[permissions.AllowAny]

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
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetail(APIView):
    """
    TODO docstring
    """
    permission_classes=[permissions.AllowAny]

    def get(self, request, pk, format=None):
        """
        TODO docstring
        """
        category = Category.objects.get(id = pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class TreeList(APIView):
    """
    TODO docstring
    """
    permission_classes=[permissions.AllowAny]

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
        serializer = TreeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

class TreeDetail(APIView):
    """
    TODO docstring
    """
    permission_classes=[permissions.AllowAny]

    def get(self, request, pk, format=None):
        """
        TODO docstring
        """
        tree = Tree.objects.get(id = pk)
        serializer = TreeSerializer(tree)
        return Response(serializer.data)

class UserList(APIView):
    """
    List all User, or create a new User.
    """
    permission_classes=[permissions.AllowAny]

    def get(self, request, format=None):
        """
        TODO docstring
        """
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        TODO docstring
        """
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    """
    TODO docstring
    """
    permission_classes=[permissions.AllowAny]

    def get(self, request, pk, format=None):
        """
        TODO docstring
        """
        user = User.objects.get(id = pk)
        serializer = ClubSerializer(user)
        return Response(serializer.data)
