from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import User,Questions,Answers
from rest_framework.viewsets import ModelViewSet
from rest_framework import authentication,permissions
from api.serializer import Userserializer
from api.models import


# Create your views here.
class Usersview(ModelViewSet):
    serializer_class = Userserializer
    queryset = User.objects.all()