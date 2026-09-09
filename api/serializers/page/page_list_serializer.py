from rest_framework import serializers

from api.models import Page


class PageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = [
            "uuid",
            "title",
            "color",
            "position",
        ]
