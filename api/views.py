from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Test view. Can be deleted when necessary
@api_view(['GET'])
def getData(request):
    person={'name':'Admin', 'number':'1'}
    return Response(person)

# Create your views here.
