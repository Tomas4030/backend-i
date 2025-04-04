# Generated by Django 5.1.7 on 2025-03-28 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("treinos", "0002_remove_treino_aluno_gymprofile_delete_aluno_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="DiaSemana",
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
                ("nome", models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name="gymprofile",
            name="altura",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.RemoveField(
            model_name="gymprofile",
            name="dias_treino",
        ),
        migrations.AlterField(
            model_name="gymprofile",
            name="objetivos",
            field=models.CharField(
                blank=True,
                choices=[
                    ("ganhar_peso", "Ganhar Peso"),
                    ("perder_peso", "Perder Peso"),
                    ("manter_peso", "Manter Peso"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="gymprofile",
            name="peso",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.AddField(
            model_name="gymprofile",
            name="dias_treino",
            field=models.ManyToManyField(blank=True, to="treinos.diasemana"),
        ),
    ]
