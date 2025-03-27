from django.contrib import admin
from gym.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    # Definindo os métodos dentro da classe UserProfileAdmin
    def get_user_username(self, obj):
        return obj.user.username  # Acessa o nome de usuário do usuário associado ao perfil

    def get_dias_treino(self, obj):
        return ", ".join([dia.name for dia in obj.dias_treino.all()])  # Exibe os dias de treino associados

    # Atualizando o list_display com os métodos da classe
    list_display = ("get_user_username", "altura", "objetivo", "get_dias_treino")  
    search_fields = ("user__username", "objetivo")  # Pesquisa por 'user__username'
    list_filter = ("objetivo",)

    get_user_username.admin_order_field = 'user__username'  # Permite ordenar pelo nome de usuário
    get_user_username.short_description = 'Username'  # Define o nome da coluna no admin
    get_dias_treino.short_description = 'Dias de Treino'  # Nome da coluna para os dias de treino

# Registrar o modelo UserProfile no painel de administração com as configurações personalizadas
admin.site.register(UserProfile, UserProfileAdmin)
