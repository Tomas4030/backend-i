from django import forms
from gym.models import Task, UserProfile,WeekDay


class UserProfileForm(forms.ModelForm):
    dias_treino = forms.ModelMultipleChoiceField(
        queryset=WeekDay.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = UserProfile
        fields = ["altura", "peso", "objetivo", "dias_treino"]