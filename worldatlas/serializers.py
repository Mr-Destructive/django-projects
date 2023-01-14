from rest_framework import serializers
from .models import Places

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Places
        fields = ('name',)
