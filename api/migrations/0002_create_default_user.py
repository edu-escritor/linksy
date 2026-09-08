import os

from django.contrib.auth.hashers import make_password
from django.db import migrations


def create_default_user(apps, schema_editor):
    user_model = apps.get_model("api", "User")

    user_model.objects.get_or_create(
        username=os.environ["DEFAULT_USER_USERNAME"],
        defaults={
            "password": make_password(os.environ["DEFAULT_USER_PASSWORD"]),
            "first_name": os.environ["DEFAULT_USER_FIRST_NAME"],
            "last_name": os.environ["DEFAULT_USER_LAST_NAME"],
            "email": os.environ["DEFAULT_USER_EMAIL"],
            "is_active": os.environ.get(
                "DEFAULT_USER_IS_ACTIVE",
                "True",
            ).lower()
            == "true",
        },
    )


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_default_user),
    ]
