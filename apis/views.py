from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserSerializer

# Create your views here.
@api_view(['POST'])
def register_new_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Status": "Added"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def index(request):
    return Response({"Status": "Added"}, status=status.HTTP_201_CREATED)