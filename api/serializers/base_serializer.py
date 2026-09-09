from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from api.enums.color import Color


# noinspection PyMethodMayBeStatic
class BaseSerializer(serializers.ModelSerializer):

    def validate_title(self, value: str) -> str:
        return value.strip()

    def validate_color(self, value: str) -> str:
        value = value.strip().lower()

        try:
            Color(value)
        except ValueError:
            raise serializers.ValidationError(_("error.invalid_color") % {"color": value})

        return value

    def validate_position(self, value: int) -> int:
        if value < 0:
            raise serializers.ValidationError(_("error.negative_position"))

        return value
