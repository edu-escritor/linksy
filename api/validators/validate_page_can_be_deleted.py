from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from api.models import Page


class ValidatePageCanBeDeleted:

    @staticmethod
    def validate(page: Page) -> None:
        count = Page.objects.filter(user=page.user).count()

        if count <= 1:
            raise serializers.ValidationError(_("error.at_least_one_page"))
