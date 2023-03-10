# Generated by Django 4.1.7 on 2023-02-19 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Network",
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
                (
                    "title",
                    models.CharField(max_length=150, verbose_name="Название сети"),
                ),
            ],
            options={
                "verbose_name": "Торговая сеть",
                "verbose_name_plural": "Торговые сети",
            },
        ),
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
                (
                    "name",
                    models.CharField(max_length=25, verbose_name="Название товара"),
                ),
                (
                    "model",
                    models.CharField(max_length=100, verbose_name="Модель продукта"),
                ),
                ("release_date", models.DateField(verbose_name="Дата выхода на рынок")),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
            },
        ),
        migrations.CreateModel(
            name="Company",
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
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("FKT", "Завод"),
                            ("DST", "Дистрибьютор"),
                            ("DLR", "Дилерский центр"),
                            ("RET", "Крупная розничная сеть"),
                            ("IP", "Индивидуальный предприниматель"),
                        ],
                        max_length=3,
                        verbose_name="Тип компании",
                    ),
                ),
                (
                    "hierarchy",
                    models.PositiveSmallIntegerField(
                        default=0, verbose_name="Уровень в иерархии"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="Название компании"
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "country",
                    models.CharField(max_length=100, verbose_name="Название страны"),
                ),
                (
                    "city",
                    models.CharField(max_length=100, verbose_name="Название города"),
                ),
                (
                    "street",
                    models.CharField(max_length=100, verbose_name="Название улицы"),
                ),
                (
                    "building_number",
                    models.CharField(max_length=50, verbose_name="Номер дома"),
                ),
                (
                    "debt",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0,
                        max_digits=20,
                        verbose_name="Задолженность",
                    ),
                ),
                ("created_date", models.DateField(auto_now_add=True)),
                (
                    "network",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="companies",
                        to="retail.network",
                        verbose_name="Торговая сеть",
                    ),
                ),
                (
                    "products",
                    models.ManyToManyField(
                        related_name="companies", to="retail.product"
                    ),
                ),
                (
                    "provider",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="traders",
                        to="retail.company",
                        verbose_name="Поставщик",
                    ),
                ),
            ],
            options={
                "verbose_name": "Компания",
                "verbose_name_plural": "Компании",
            },
        ),
    ]
