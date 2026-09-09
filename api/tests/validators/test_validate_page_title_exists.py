from django.test import TestCase
from rest_framework import serializers

from api.models import Page, User
from api.validators.validate_page_title_exists import ValidatePageTitleExists


class ValidatePageTitleExistsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            first_name="Test",
            last_name="User",
            password="12345678",
        )

        self.other_user = User.objects.create_user(
            username="otheruser",
            email="other@example.com",
            first_name="Other",
            last_name="User",
            password="12345678",
        )

    def test_allows_new_title(self):
        ValidatePageTitleExists.validate(
            title="Work",
            user=self.user,
        )

    def test_raises_when_title_already_exists_for_same_user(self):
        Page.objects.create(
            user=self.user,
            title="Work",
        )

        with self.assertRaises(serializers.ValidationError):
            ValidatePageTitleExists.validate(
                title="Work",
                user=self.user,
            )

    def test_allows_same_title_for_different_user(self):
        Page.objects.create(
            user=self.other_user,
            title="Work",
        )

        ValidatePageTitleExists.validate(
            title="Work",
            user=self.user,
        )

    def test_allows_same_title_when_updating_same_page(self):
        page = Page.objects.create(
            user=self.user,
            title="Work",
        )

        ValidatePageTitleExists.validate(
            title="Work",
            user=self.user,
            page=page,
        )

    def test_raises_when_updating_to_existing_title(self):
        page = Page.objects.create(
            user=self.user,
            title="Personal",
        )

        Page.objects.create(
            user=self.user,
            title="Work",
        )

        with self.assertRaises(serializers.ValidationError):
            ValidatePageTitleExists.validate(
                title="Work",
                user=self.user,
                page=page,
            )
