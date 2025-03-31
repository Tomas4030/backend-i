import logging
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from .models import GymProfile
from .forms import GymProfileForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .utils import obter_exercicios_objetivo

logger = logging.getLogger(__name__)

def plano_de_treino(request):
    treino_plano = obter_exercicios_objetivo()

    logger.info(f"Treino criado: {treino_plano}") 

    return render(request, "gym/plano_de_treino.html", {"treino_plano": treino_plano})

# Atualiza o perfil de ginásio do utilizador logado
class GymProfileCreateView(LoginRequiredMixin, CreateView):
    model = GymProfile
    form_class = GymProfileForm
    template_name = "gym/gym_profile_form.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Atribui o utilizador logado ao campo 'user'
        
        # Registra a ação de atualização ou criação do perfil
        try:
            gym_profile = GymProfile.objects.get(user=self.request.user)
            gym_profile.altura = form.cleaned_data.get('altura')
            gym_profile.peso = form.cleaned_data.get('peso')
            gym_profile.objetivos = form.cleaned_data.get('objetivos')
            gym_profile.dias_treino = form.cleaned_data.get('dias_treino')
            gym_profile.save()  
            logger.info(f"Perfil atualizado para o utilizador {self.request.user.username}.")
            return redirect(self.success_url)
        except GymProfile.DoesNotExist:
            logger.info(f"Criando novo perfil para o utilizador {self.request.user.username}.")
            return super().form_valid(form)

# Página inicial com login e cadastro
class IndexView(TemplateView):
    template_name = "gym/index.html"

# View para cadastro de utilizador
class SignUpView(FormView):
    template_name = "registration/signup.html"
    success_url = "/login"
    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        logger.info(f"Novo utilizador registado: {form.cleaned_data['username']}.")
        return super().form_valid(form)

# View para login
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = '/home'

    def form_valid(self, form):
        logger.info(f"Utilizador {form.cleaned_data['username']} fez login com sucesso.")
        return super().form_valid(form)

# Função de logout
def logout_view(request):
    logger.info(f"Utilizador {request.user.username} fez logout.")
    logout(request)
    return redirect("/")   

# Página inicial
def home(request):
    if request.user.is_authenticated:
        gym_profile = GymProfile.objects.filter(user=request.user).first()
        logger.info(f"Utilizador {request.user.username} acessou a página inicial.")
    else:
        gym_profile = None
        logger.info("Utilizador não autenticado acessou a página inicial.")
    
    return render(request, 'gym/home.html', {'gym_profile': gym_profile})
