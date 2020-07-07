
from django.shortcuts import render
from .models import postcard
from .serializers import postcardSerializer
from rest_framework import generics


class postcardListCreate(generics.ListCreateAPIView):
    queryset = postcard.objects.all()
    serializer_class = postcardSerializer


class postcarddetail(generics.RetrieveAPIView):
    queryset = postcard.objects.all()
    serializer_class = postcardSerializer
