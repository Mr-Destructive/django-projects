import random
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .models import Places
from .serializers import PlaceSerializer

class PlaceViewSet(ModelViewSet):
    queryset = Places.objects.all()
    serializer_class = PlaceSerializer

    @action(detail=False, methods=['GET',], url_path='lists/(?P<letter>[^/.]+)')
    def lists(self, request, letter:str):
        places = Places.objects.filter(name__startswith=letter).values_list(
            "name", flat=True
        )
        return JsonResponse({letter: list(places)})
    
    @action(detail=False, methods=['GET',], url_path='get/(?P<letter>[^/.]+)')
    def get_random_place(self, request, letter):
        places = Places.objects.filter(name__startswith=letter).values_list('name', flat=True)
        place = random.choice(places)
        return JsonResponse({letter: place})
    
    @action(detail=False, methods=['GET',], url_path='exists/(?P<place>[^/.]+)')
    def place_exists(self, request, place):
        place_exists = Places.objects.filter(name=place).exists()
        if place_exists:
            return JsonResponse({"result": True})
        else:
            return JsonResponse({"result": False})

