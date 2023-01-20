from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from .views import PlaceViewSet, world_atlas, world_atlas_bot, world_atlas_play

router = routers.SimpleRouter()
router.register("places", PlaceViewSet)

urlpatterns = [
        path("api/", TemplateView.as_view(template_name='world-atlas-api.html')),
        path("api/", include(router.urls), name='api'),
        path("", world_atlas, name='world-atlas'),
        path("play/", world_atlas_play, name='world-atlas-play'),
        path("bot/", world_atlas_bot, name='world-atlas-bot'),
]
