import hashlib
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GRAVATAR = "https://www.gravatar.com/avatar"

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    email = models.EmailField(
        unique=True,
        blank=False,
    )

    first_name = models.CharField(
        max_length=150,
        blank=False,
    )

    last_name = models.CharField(
        max_length=150,
        blank=False,
    )

    @property
    def gravatar(self) -> str:
        email = self.email.strip().lower()
        email_hash = hashlib.sha256(email.encode("utf-8")).hexdigest()

        return f"{self.GRAVATAR}/{email_hash}"

    class Meta:
        db_table = "users"
