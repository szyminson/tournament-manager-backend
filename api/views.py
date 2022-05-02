from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from api.models import User, Participant, Club, VerificationCode
from rest_framework.views import APIView
from rest_framework import status
from django.core import serializers

from api.serializers import ClubSerializer, VerificationCodeSerializer

#permission_classes = [permissions.AllowAny]

## Test view. Can be deleted when necessary
#@api_view(['GET'])
#def getData(request):
#    person={'name':'Admin', 'number':'1'}
#    return Response(person)
#
## Create your views here.
#@api_view(['GET'])
#@permission_classes([permissions.AllowAny])
#def createUser(request):
#    user = User(username="workata", email="cos@gmail.com", hashed_password="1234", user_type= User.UserType.ADMINISTRATOR)
#    user.save()
#    return Response(user)
#
#@api_view(['GET'])
#@permission_classes([permissions.IsAuthenticated])
#def superEndpoint(request):
#    return Response({'xd': 'xdddddd'})
#

class ParticipantList(APIView):
    """
    List all Participants, or create a new Participant.
    """
    # * for testing allow any for all endopints in this class
    permission_classes=[permissions.AllowAny]
    # def get(self, request, format=None):
    #     snippets = Snippet.objects.all()
    #     serializer = SnippetSerializer(snippets, many=True)
    #     return Response(serializer.data)

    def post(self, request, format=None):
        # TODO validation / serializers?
        return Response(request.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ParticipantDetail(APIView):

#     def get(self, request, format=None):
#         return Response({'test': 'test'})

class ClubList(APIView):
    """
    List all Clubs, or create a new Club.
    """
    permission_classes=[permissions.AllowAny]

    def get(self, request, format=None):
        clubs = Club.objects.all()
        serializer = ClubSerializer(clubs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClubSerializer(request.data, many=True)
        if serializer.is_valid():
            club = Club(club_name = request.data['club_name'], club_ceo = request.data['club_ceo'])
            club.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

class ClubDetail(APIView):
    permission_classes=[permissions.AllowAny]

    def get(self, request, pk, format=None):
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
        serializer = VerificationCodeSerializer(request.data, many=True)
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
