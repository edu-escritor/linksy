from django.test import TestCase
from rest_framework.exceptions import PermissionDenied
from rest_framework.serializers import ValidationError

from api.handlers.page_handler import PageHandler
from api.models import Page, User


class PageHandlerTest(TestCase):

    def setUp(self):
        self.handler = PageHandler()

        self.user = User.objects.create_user(
            username="user1",
            email="user1@example.com",
            first_name="User",
            last_name="One",
            password="12345678",
        )

        self.other_user = User.objects.create_user(
            username="user2",
            email="user2@example.com",
            first_name="User",
            last_name="Two",
            password="12345678",
        )

    def test_create_page(self):
        page = self.handler.create(
            user=self.user,
            data={
                "title": "Work",
                "color": "#ffffff",
                "position": 0,
            },
        )

        self.assertEqual(page.user, self.user)
        self.assertEqual(page.title, "Work")
        self.assertTrue(Page.objects.filter(pk=page.pk).exists())

    def test_create_duplicate_title_raises_validation_error(self):
        Page.objects.create(
            user=self.user,
            title="Work",
        )

        with self.assertRaises(ValidationError):
            self.handler.create(
                user=self.user,
                data={
                    "title": "Work",
                    "color": "#ffffff",
                    "position": 0,
                },
            )

    def test_list_returns_only_user_pages(self):
        Page.objects.create(
            user=self.user,
            title="Work",
        )

        Page.objects.create(
            user=self.other_user,
            title="Personal",
        )

        pages = self.handler.list(self.user)

        self.assertEqual(pages.count(), 1)
        self.assertEqual(pages.first().title, "Work")

    def test_retrieve_returns_owned_page(self):
        page = Page.objects.create(
            user=self.user,
            title="Work",
        )

        result = self.handler.retrieve(
            user=self.user,
            page=page,
        )

        self.assertEqual(result, page)

    def test_retrieve_other_user_page_raises_permission_denied(self):
        page = Page.objects.create(
            user=self.other_user,
            title="Work",
        )

        with self.assertRaises(PermissionDenied):
            self.handler.retrieve(
                user=self.user,
                page=page,
            )

    def test_update_page(self):
        page = Page.objects.create(
            user=self.user,
            title="Work",
        )

        updated_page = self.handler.update(
            user=self.user,
            page=page,
            data={
                "title": "Personal",
            },
        )

        self.assertEqual(updated_page.title, "Personal")

        page.refresh_from_db()
        self.assertEqual(page.title, "Personal")

    def test_update_to_existing_title_raises_validation_error(self):
        page = Page.objects.create(
            user=self.user,
            title="Work",
        )

        Page.objects.create(
            user=self.user,
            title="Personal",
        )

        with self.assertRaises(ValidationError):
            self.handler.update(
                user=self.user,
                page=page,
                data={
                    "title": "Personal",
                },
            )

    def test_update_other_user_page_raises_permission_denied(self):
        page = Page.objects.create(
            user=self.other_user,
            title="Work",
        )

        with self.assertRaises(PermissionDenied):
            self.handler.update(
                user=self.user,
                page=page,
                data={
                    "title": "Personal",
                },
            )

    def test_delete_page(self):
        page = Page.objects.create(
            user=self.user,
            title="Work",
        )

        Page.objects.create(
            user=self.user,
            title="Personal",
        )

        self.handler.delete(
            user=self.user,
            page=page,
        )

        self.assertFalse(Page.objects.filter(pk=page.pk).exists())

    def test_delete_last_page_raises_validation_error(self):
        page = Page.objects.create(
            user=self.user,
            title="Work",
        )

        with self.assertRaises(ValidationError):
            self.handler.delete(
                user=self.user,
                page=page,
            )

    def test_delete_other_user_page_raises_permission_denied(self):
        page = Page.objects.create(
            user=self.other_user,
            title="Work",
        )

        with self.assertRaises(PermissionDenied):
            self.handler.delete(
                user=self.user,
                page=page,
            )
