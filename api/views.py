"""
TODO module docstring
"""

from unicodedata import category
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from api.models import Category, Tournament, Tree, User, Participant, Club, VerificationCode, Duel, User
from rest_framework.views import APIView
from rest_framework import status
from django.core import serializers

from api.serializers import CategorySerializer, ClubSerializer, TournamentSerializer, TreeSerializer, VerificationCodeSerializer, DuelSerializer, UserSerializer, ParticipantSerializer




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
        participants = Participant.objects.all()
        serializer = ParticipantSerializer(participants, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ParticipantSerializer(data = request.data)
        if serializer.is_valid():
            participant = Participant(
                first_name = request.data['first_name'],
                last_name = request.data['last_name'],
                gender = request.data['gender'],
                date_of_birth = request.data['date_of_birth'],
                club = request.data['club'],
                verification_code = request.data['verification_code'],
                )
            participant.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

class ParticipantDetail(APIView):
    permission_classes=[permissions.AllowAny]

    def get(self, request, pk, format=None):
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
            club = Club(club_name = request.data['club_name'], club_ceo = request.data['club_ceo'])
            club.save()
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
        verification_code = VerificationCode.objects.all()
        serializer = VerificationCodeSerializer(verification_code, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VerificationCodeSerializer(data = request.data)
        if serializer.is_valid():
            verification_code = VerificationCode(
                code = request.data['code'],
                participants_limit = request.data['participants_limit'],
                club = request.data['club']
                )
            verification_code.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

class VerificationCodeDetail(APIView):
    permission_classes=[permissions.AllowAny]

    def get(self, request, pk, format=None):
        duel = VerificationCode.objects.get(id = pk)
        serializer = VerificationCodeSerializer(duel)
        return Response(serializer.data)

class DuelList(APIView):
    """
    List all Duels, or create a new Duel.
    """
    permission_classes=[permissions.AllowAny]

    def get(self, request, format=None):
        duels = Duel.objects.all()
        serializer = DuelSerializer(duels, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DuelSerializer(data = request.data)
        if serializer.is_valid():
            duel = duel(participant_one = request.data['participant_one'], participant_two = request.data['participant_two'],
            parent_duel = request.data['parent_duel'], winner = request.data['winner'], score_description = request.data['score_description'])
            duel.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

class DuelDetail(APIView):
    permission_classes=[permissions.AllowAny]

    def get(self, request, pk, format=None):
        duel = Duel.objects.get(id = pk)
        serializer = DuelSerializer(duel)
        return Response(serializer.data)

class TournamentList(APIView):
    permission_classes=[permissions.AllowAny]

    def get(self, request, format=None):
        tournaments = Tournament.objects.all()
        serializer = TournamentSerializer(tournaments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TournamentSerializer(data = request.data)
        if serializer.is_valid():
            tree = Tournament(time = request.data['time'], date = request.data['date'], location = request.data['location'])
            tree.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

class TournamentDetail(APIView):
    permission_classes=[permissions.AllowAny]

    def get(self, request, pk, format=None):
        tournament = Tournament.objects.get(id = pk)
        serializer = TournamentSerializer(tournament)
        return Response(serializer.data)


class CategoryList(APIView):
    permission_classes=[permissions.AllowAny]

    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            category = Category(category_name = request.data['category_name'], description = request.data['description'])
            category.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetail(APIView):
    permission_classes=[permissions.AllowAny]

    def get(self, request, pk, format=None):
        category = Category.objects.get(id = pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class TreeList(APIView):
    permission_classes=[permissions.AllowAny]

    def get(self, request, format=None):
        trees = Tree.objects.all()
        serializer = TreeSerializer(trees, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TreeSerializer(data = request.data)
        if serializer.is_valid():
            tree = Tree(category = request.data['category'], root_duel = request.data['root_duel'], tournament = request.data['tournament'])
            tree.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

class TreeDetail(APIView):
    permission_classes=[permissions.AllowAny]

    def get(self, request, pk, format=None):
        tree = Tree.objects.get(id = pk)
        serializer = TreeSerializer(tree)
        return Response(serializer.data)

class UserList(APIView):
    """
    List all User, or create a new User.
    """
    permission_classes=[permissions.AllowAny]

    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user = User(
             username = request.data['username'],
             email = request.data['email'],
             hashed_password = request.data['hashed_password'],
             user_type = request.data['user_type']
             )
            user.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    permission_classes=[permissions.AllowAny]

    def get(self, request, pk, format=None):
        user = User.objects.get(id = pk)
        serializer = ClubSerializer(user)
        return Response(serializer.data)