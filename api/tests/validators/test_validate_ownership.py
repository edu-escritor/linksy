from types import SimpleNamespace

from django.test import SimpleTestCase
from rest_framework.exceptions import PermissionDenied

from api.validators.validate_ownership import ValidateOwnership


class ValidateOwnershipTest(SimpleTestCase):

    def test_object_without_user_passes(self):
        obj = SimpleNamespace()

        ValidateOwnership.validate(
            user=object(),
            obj=obj,
        )

    def test_object_with_same_user_passes(self):
        user = object()
        obj = SimpleNamespace(user=user)

        ValidateOwnership.validate(
            user=user,
            obj=obj,
        )

    def test_object_with_different_user_raises_permission_denied(self):
        user = object()
        obj = SimpleNamespace(user=object())

        with self.assertRaises(PermissionDenied):
            ValidateOwnership.validate(
                user=user,
                obj=obj,
            )
