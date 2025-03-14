# Generated by Django 5.1.6 on 2025-02-17 13:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=100)),
                ("opis", models.TextField()),
                ("cena", models.IntegerField(default=0)),
                (
                    "kategorija",
                    models.CharField(
                        choices=[
                            ("Kafe", "Kafe"),
                            ("Caj", "Caj"),
                            ("Voda", "Voda"),
                            ("Cedeni Sokovi", "Cedeni Sokovi"),
                            ("Sokovi", "Sokovi"),
                            ("Topli Napitoci", "Topli Napitoci"),
                            ("Pivo", "Pivo"),
                            ("Alkoholni Pijaloci", "Alkoholni Pijaloci"),
                            ("Energetski Pijaloci", "Energetski Pijaloci"),
                            ("Kokteli", "Kokteli"),
                            ("Vino", "Vino"),
                            ("Sampanj", "Sampanj"),
                            ("Bezalkoholni Kokteli", "Bezalkoholni Kokteli"),
                            ("Nargile", "Nargile"),
                            ("Apetisani", "Apetisani"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, default=None, null=True, upload_to="produkt/"
                    ),
                ),
                (
                    "kreator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
