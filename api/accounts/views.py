from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets,status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,CreateAPIView

