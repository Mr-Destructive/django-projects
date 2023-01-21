from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register("places", views.PlaceViewSet)

urlpatterns = [
        path("api/", TemplateView.as_view(template_name='world-atlas-api.html')),
        path("api/", include(router.urls), name='api'),
        path("", views.world_atlas, name='world-atlas'),
        path("play/", views.world_atlas_play, name='world-atlas-play'),
        path("bot/", views.world_atlas_bot, name='world-atlas-bot'),
        path("room/wa/<str:name>/", views.world_atlas_room, name='world-atlas-room'),
        path("room/create/", views.world_atlas_room_create, name='world-atlas-room-create'),
        path("room/join/", views.world_atlas_room_join, name='world-atlas-room-join'),
]
