from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from api.models import Page, User


class ValidatePageTitleExists:

    @staticmethod
    def validate(title: str, user: User, page: Page | None = None) -> None:
        if page is not None and page.title == title.strip():
            return

        queryset = Page.objects.filter(
            user=user,
            title=title,
        )

        if page is not None:
            queryset = queryset.exclude(pk=page.pk)

        if queryset.exists():
            raise serializers.ValidationError({"title": _("error.title_exists")})
