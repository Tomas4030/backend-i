from django.db import models
from django.contrib.auth.models import User

class GymProfile(models.Model):
    OBJETIVO_CHOICES = [
        ('ganhar_peso', 'Ganhar Peso'),
        ('perder_peso', 'Perder Peso'),
        ('manter_peso', 'Manter Peso'),
    ]
    
    DIAS_CHOICES = [
        ('2_3', '2-3 dias por semana'),
        ('3_4', '3-4 dias por semana'),
        ('4_5', '4-5 dias por semana'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    altura = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    objetivos = models.CharField(max_length=20, choices=OBJETIVO_CHOICES, null=True, blank=True)
    dias_treino = models.CharField(max_length=20, choices=DIAS_CHOICES, null=True, blank=True)
    
    def __str__(self):
        return f"Perfil de {self.user.username}"
