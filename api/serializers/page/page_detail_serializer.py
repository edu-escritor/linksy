from api.models import Page
from api.serializers.base_serializer import BaseSerializer


class PageDetailSerializer(BaseSerializer):
    class Meta:
        model = Page
        fields = [
            "uuid",
            "title",
            "color",
            "position",
            "created_at",
            "updated_at",
        ]
