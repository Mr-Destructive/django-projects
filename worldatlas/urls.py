from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from .views import PlaceViewSet

router = routers.SimpleRouter()
router.register("places", PlaceViewSet)

urlpatterns = [
        path("api/", TemplateView.as_view(template_name='world-atlas-api.html')),
        path("api/", include(router.urls), name='api'),
        #path('api/get/<str:letter>/', GetPlace.as_view(), name='get-place-letter'),
        #path('api/place/<str:place>/', PlaceExist.as_view(), name='place-exist'),
        #path('api/list/<str:letter>/', ListPlaces.as_view(), name='place-list'),
]
