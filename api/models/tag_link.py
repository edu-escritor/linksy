import uuid

from django.db import models


class TagLink(models.Model):

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    tag = models.ForeignKey(
        "Tag",
        on_delete=models.CASCADE,
    )

    link = models.ForeignKey(
        "Link",
        on_delete=models.CASCADE,
    )

    position = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "tags_links"
        ordering = ["position", "link__title"]
        constraints = [
            models.UniqueConstraint(
                fields=["tag", "link"],
                name="unique_link_per_tag",
            ),
        ]
