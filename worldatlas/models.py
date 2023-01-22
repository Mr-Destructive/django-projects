import random
from django.db import models

class Places(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Room(models.Model):

    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def generate_random_turn():
        return random.randint(0,1)

    first_turn = models.IntegerField(blank=True, default=generate_random_turn)

    def __str__(self):
        return self.name

