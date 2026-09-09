from typing import cast

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.handlers.page_handler import PageHandler
from api.models import Page, User
from api.serializers.page.page_detail_serializer import PageDetailSerializer
from api.serializers.page.page_list_serializer import PageListSerializer


# noinspection PyMethodMayBeStatic
class PageViewSet(ModelViewSet):
    queryset = Page.objects.none()
    lookup_field = "uuid"

    def get_serializer_class(self):
        if self.action == "list":
            return PageListSerializer

        return PageDetailSerializer

    def list(self, request, *args, **kwargs):
        user = cast(User, request.user)

        pages = PageHandler().list(user)

        serializer = self.get_serializer(
            pages,
            many=True,
        )

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):

        page = PageHandler().retrieve(user=self._get_user(request), page=self.get_object())

        serializer = self.get_serializer(page)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        page = PageHandler().create(
            user=self._get_user(request),
            data=serializer.validated_data,
        )

        response_serializer = self.get_serializer(page)

        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, *args, **kwargs):
        page = self.get_object()

        serializer = self.get_serializer(page, data=request.data)
        serializer.is_valid(raise_exception=True)

        page = PageHandler().update(
            user=self._get_user(request),
            page=page,
            data=serializer.validated_data,
        )

        return Response(self.get_serializer(page).data)

    def partial_update(self, request, *args, **kwargs):
        page = self.get_object()

        serializer = self.get_serializer(
            page,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)

        page = PageHandler().update(
            user=self._get_user(request),
            page=page,
            data=serializer.validated_data,
        )

        return Response(self.get_serializer(page).data)

    def destroy(self, request, *args, **kwargs):
        PageHandler().delete(
            user=self._get_user(request),
            page=self.get_object(),
        )

        return Response(status=status.HTTP_204_NO_CONTENT)

    def _get_user(self, request: Request) -> User:
        return cast(User, request.user)
