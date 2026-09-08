import uuid

from django.conf import settings
from django.db import models

from api.enums.color import Color


class Tag(models.Model):

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
        blank=False,
    )

    color = models.CharField(
        max_length=7,
        default=Color.WHITE.value,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tags"
        ordering = ["title"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "title"],
                name="unique_tag_title_per_user",
            ),
        ]
