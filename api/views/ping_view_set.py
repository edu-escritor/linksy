from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class PingViewSet(ViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=["get"])
    def retrieve(self, request):
        return Response(
            "pong",
            status=status.HTTP_200_OK,
        )
