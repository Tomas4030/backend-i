from django.contrib import admin
from gym.models import Task, UserProfile  

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "due_date", "is_done")
    list_editable = ("due_date", "is_done")
    sortable_by = ("due_date", "is_done", "title")

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "altura", "peso", "get_dias_treino")

    def get_dias_treino(self, obj):
        return ", ".join([dia.name for dia in obj.dias_treino.all()])
    
    get_dias_treino.short_description = "Dias de Treino"


admin.site.register(Task, TaskAdmin)
admin.site.register(UserProfile, UserProfileAdmin) 
