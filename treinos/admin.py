 # admin.py
from django.contrib import admin
from .models import GymProfile

class GymProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'altura', 'peso', 'objetivos', 'dias_treino')  
    search_fields = ('user__username',)  

admin.site.register(GymProfile, GymProfileAdmin)
