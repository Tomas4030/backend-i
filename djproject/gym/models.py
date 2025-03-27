from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth import get_user_model

# Modelo de Dias da Semana
class WeekDay(models.Model):
    WEEK_DAYS = [
        ("segunda", "Segunda-feira"),
        ("terca", "Terça-feira"),
        ("quarta", "Quarta-feira"),
        ("quinta", "Quinta-feira"),
        ("sexta", "Sexta-feira"),
        ("sabado", "Sábado"),
        ("domingo", "Domingo"),
    ]

    name = models.CharField(max_length=10, choices=WEEK_DAYS, unique=True)

    def __str__(self):
        return self.get_name_display()

# Modelo de Perfil de Utilizador
class UserProfile(models.Model):
    OBJECTIVE_CHOICES = [
        ("perda_peso", "Perda de Peso"),
        ("ganho_massa", "Ganho de Massa"),
        ("resistencia", "Melhorar Resistência"),
    ]

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    altura = models.FloatField()
    peso = models.FloatField()
    objetivo = models.CharField(max_length=20, choices=OBJECTIVE_CHOICES)
    dias_treino = models.ManyToManyField(WeekDay)

    class Meta:
        db_table = "gym_user_profiles"

# Modelo de Tarefas
class Task(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField()
    due_date = models.DateField(null=True)
    is_done = models.BooleanField(null=False, blank=False, default=False)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True
    )

    class Meta:
        db_table = "gym_tasks"
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
