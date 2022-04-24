from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from api.models import User
from rest_framework.views import APIView

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
class UserList(APIView):
    permission_classes=[permissions.AllowAny]

    #@permission_classes([permissions.IsAuthenticated])
    def get(self, request, format=None):
        return Response({'test': 'test'})

class UserDetail(APIView):
    permission_classes=[permissions.AllowAny]
    def get(self, request, pk, format=None):
        return Response({'id': pk})