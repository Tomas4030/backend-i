from django import forms
from .models import GymProfile

class GymProfileForm(forms.ModelForm):
    
    # Campo de objetivo (radiobuttons)
    objetivos = forms.ChoiceField(
        choices=GymProfile.OBJETIVO_CHOICES,
        widget=forms.RadioSelect, 
        label="Objetivo",
        required=True
    )

    # Campo de dias de treino (radiobuttons)
    dias_treino = forms.ChoiceField(
        choices=GymProfile.DIAS_CHOICES,
        widget=forms.RadioSelect, 
        label="Dias de treino",
        required=True
    )
    
    class Meta:
        model = GymProfile
        fields = ['altura', 'peso', 'objetivos', 'dias_treino']
