# Generated by Django 4.2.9 on 2024-05-04 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_of_birth", models.DateField(blank=True, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ChatMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.TextField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_messages",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sent_messages",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="chat_model",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("mas", models.CharField(max_length=250)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("outher", models.CharField(max_length=250)),
                ("slug", models.SlugField(max_length=200)),
                (
                    "photo_book",
                    models.ImageField(blank=True, null=True, upload_to="photos"),
                ),
                (
                    "photo_outher",
                    models.ImageField(blank=True, null=True, upload_to="photos"),
                ),
                ("pages", models.IntegerField(blank=True, null=True)),
                (
                    "price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "retal_price_day",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("retal_period", models.IntegerField(blank=True, null=True)),
                (
                    "total_rental",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("active", models.BooleanField(blank=True, default=True)),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("availble", "availble"),
                            ("rental", "rental"),
                            ("sold", "sold"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                ("open_book", models.FileField(upload_to="files")),
                ("description", models.TextField()),
                ("views", models.IntegerField(blank=True, default=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "Category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="blog.category",
                    ),
                ),
            ],
        ),
    ]
