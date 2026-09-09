from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import PermissionDenied


class ValidateOwnership:

    @staticmethod
    def validate(user, obj) -> None:
        if not hasattr(obj, "user"):
            return

        if obj.user != user:
            raise PermissionDenied(_("error.no_permission"))
        return
