
from django.shortcuts import render
from .models import postcard, subscribers
from .serializers import postcardSerializer, subscribersSerialize
from rest_framework import generics


class postcardListCreate(generics.ListCreateAPIView):
    queryset = postcard.objects.all().order_by('id')
    serializer_class = postcardSerializer


class postcarddetail(generics.RetrieveAPIView):
    queryset = postcard.objects.all()
    serializer_class = postcardSerializer


class subscribers(generics.ListCreateAPIView):
    queryset = subscribers.objects.all()
    serializer_class = subscribersSerialize
