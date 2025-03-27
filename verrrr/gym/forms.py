from django import forms
from gym.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['altura', 'objetivo', 'dias_treino']