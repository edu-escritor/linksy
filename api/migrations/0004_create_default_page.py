import os

from django.db import migrations

from api.enums.color import Color


def create_default_page(apps, schema_editor):
    user_model = apps.get_model("api", "User")
    page_model = apps.get_model("api", "Page")

    user = user_model.objects.get(
        username=os.environ["DEFAULT_USER_USERNAME"],
    )

    page_model.objects.get_or_create(
        user=user,
        title="Linksy",
        defaults={
            "color": Color.WHITE.value,
        },
    )


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_page"),
    ]

    operations = [
        migrations.RunPython(create_default_page),
    ]
