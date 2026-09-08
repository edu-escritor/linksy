import uuid

from django.db import models


class PageTag(models.Model):

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    page = models.ForeignKey(
        "Page",
        on_delete=models.CASCADE,
    )

    tag = models.ForeignKey(
        "Tag",
        on_delete=models.CASCADE,
    )

    position = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "pages_tags"
        ordering = ["position", "tag__title"]
        constraints = [
            models.UniqueConstraint(
                fields=["page", "tag"],
                name="unique_tag_per_page",
            ),
        ]
