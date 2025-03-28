from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from .models import GymProfile
from .forms import GymProfileForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Atualiza o perfil de ginásio do usuário logado
class GymProfileCreateView(LoginRequiredMixin, CreateView):
    model = GymProfile
    form_class = GymProfileForm
    template_name = "gym/gym_profile_form.html"

    # Redireciona para a página de edição se o usuário já tiver um perfil de ginásio
    def get(self, request, *args, **kwargs):
        try:
            # Verificar se o usuário já tem um perfil de ginásio
            gym_profile = GymProfile.objects.get(user=request.user)
            return redirect('gym_profile_edit')  # Redireciona para a página de edição
        except GymProfile.DoesNotExist:
            return super().get(request, *args, **kwargs)  # Caso contrário, cria um novo perfil

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('home')
    

# Página inicial com login e cadastro
class IndexView(TemplateView):
    http_method_names = ['get']
    template_name = "gym/index.html"

# View para cadastro de usuário
class SignUpView(FormView):
    template_name = "registration/signup.html"
    success_url = "/login"
    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# View para login
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = '/home'

# Função de logout
def logout_view(request):
    logout(request)
    return redirect("/")   

# Página home (após login)
def home(request):
    # Verificar se o usuário tem um perfil de ginásio
    try:
        request.user.gymprofile
    except GymProfile.DoesNotExist:
        return redirect('gym_profile_form')  # Redireciona para criar o perfil
    return render(request, 'gym/home.html')  # Caso contrário, renderiza a home
