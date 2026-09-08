import uuid

from django.conf import settings
from django.db import models


class Link(models.Model):

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )

    title = models.CharField(
        max_length=120,
        null=True,
        blank=False,
    )

    url = models.URLField(
        max_length=2048,
        blank=False,
    )

    favicon = models.URLField(
        max_length=2048,
        null=True,
        blank=False,
    )

    notes = models.TextField(
        null=True,
        blank=False,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "links"
        ordering = ["title"]
