import random
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .models import Places, Room
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

def world_atlas_play(request):
    return render(request,'world-atlas/play.html')

def world_atlas(request):
    return render(request,'world-atlas/index.html')

def world_atlas_bot(request):
    return render(request,'world-atlas/bot.html')

def world_atlas_room(request, name):
    slug = Room.objects.get(name=name).slug
    return render(request, 'world-atlas/room.html', {'name': name, 'slug': slug})

def world_atlas_room_create(request):
    #create a room
    if request.method == "POST":
        room_name = request.POST["room_name"]
        Room.objects.create(name=room_name, slug=room_name)
        slug = Room.objects.get(name=room_name).slug
        return redirect(reverse('world-atlas-room', kwargs={'name': room_name}))
    else:
        return render(request, 'world-atlas/user-room.html')

def world_atlas_room_join(request):
    if request.method == "POST":
        room_name = request.POST["room_name"]
        return redirect(reverse('world-atlas-room', kwargs={'name': room_name}))
    else:
        return render(request, 'world-atlas/user-join.html')
