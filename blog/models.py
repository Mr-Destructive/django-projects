from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.db import models
from djnotes.models import TimeStampedModel
from user.models import User



class Tags(TimeStampedModel):
    ...


class Series(TimeStampedModel):
    ...


class Article(TimeStampedModel):
    class Article_Status(models.TextChoices):
        DRAFT = (
            "DRAFT",
            _("Draft"),
        )
        PUBLISHED = (
            "PUBLISHED",
            _("Published"),
        )

    title = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=256)
    content = models.TextField(default="", null=False, blank=False, unique=True)
    image_link = models.URLField(null=True, blank=True)
    status = models.CharField(
        max_length=16,
        choices=Article_Status.choices,
        default=Article_Status.DRAFT,
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")

    def __str__(self):
        return self.title

    def get_absolute_url(self):      
        return reverse('articles:article-detail', args=[str(self.id)])

