from django.test import TestCase
from rest_framework import serializers

from api.models import Page, User
from api.validators.validate_page_can_be_deleted import ValidatePageCanBeDeleted


class ValidatePageCanBeDeletedTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            first_name="Test",
            last_name="User",
            password="12345678",
        )

    def test_allows_delete_when_user_has_more_than_one_page(self):
        page = Page.objects.create(
            user=self.user,
            title="Page 1",
        )

        Page.objects.create(
            user=self.user,
            title="Page 2",
        )

        ValidatePageCanBeDeleted.validate(page)

    def test_raises_validation_error_when_user_has_only_one_page(self):
        page = Page.objects.create(
            user=self.user,
            title="Page 1",
        )

        with self.assertRaises(serializers.ValidationError):
            ValidatePageCanBeDeleted.validate(page)
