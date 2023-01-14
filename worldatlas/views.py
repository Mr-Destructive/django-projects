import random
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import Places
from .serializers import PlaceSerializer

class PlaceViewSet(ModelViewSet):
    queryset = Places.objects.all()
    serializer_class = PlaceSerializer

class GetPlace(APIView):
    def get(self, request, letter):
        places = Places.objects.filter(name__startswith=letter).values_list('name', flat=True)
        place = random.choice(places)
        return JsonResponse({letter: place})
