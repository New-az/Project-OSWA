from django.shortcuts import render
from mainpage.models import Card
from mainpage.serializers import CardSerializer
from rest_framework import generics

class CardListCreate(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer