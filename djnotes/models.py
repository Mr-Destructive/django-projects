from django.db import models
from user.models import User


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Note(TimeStampedModel):
    name = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.name


class Tag(TimeStampedModel):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Notebook(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="book_writer"
    )
    notes = models.ManyToManyField(
        Note,
        related_name="booknotes",
        blank=True,
        null=True,
    )
    tags = models.ManyToManyField(
            Tag,
            related_name="booktags",
            blank=True,
            null=True,
    )

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.name

