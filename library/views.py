from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework import generics
from rest_framework import authentication
from django.contrib.auth import authenticate, login, logout

from .models import *
from .serializers import *
from .permissions import *

# Create your views here.


def welcome_page(request):
    return render(request, 'library/index.html')

