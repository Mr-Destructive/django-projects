from django.urls import path, include
from rest_framework import routers
from .views import PlaceViewSet, GetPlace

router = routers.SimpleRouter()
router.register("places", PlaceViewSet)

urlpatterns = [
        path("", include(router.urls), name='api'),
        path('get/<str:letter>/', GetPlace.as_view(), name='get-place-letter'),
]
