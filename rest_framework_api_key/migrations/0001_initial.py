# Generated by Django 2.0.7 on 2018-07-28 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="APIKey",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "client_id",
                    models.CharField(
                        help_text="A free-form unique identifier of the client. 50 characters max.",
                        max_length=50,
                        unique=True,
                    ),
                ),
                ("key", models.CharField(max_length=40, unique=True)),
                ("revoked", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "API key",
                "verbose_name_plural": "API keys",
                "ordering": ("-created",),
            },
        )
    ]
