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
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Atribui explicitamente o usuário logado ao campo 'user'
        form.instance.user = self.request.user

        try:
            gym_profile = GymProfile.objects.get(user=self.request.user)
            gym_profile.altura = form.cleaned_data.get('altura')
            gym_profile.peso = form.cleaned_data.get('peso')
            gym_profile.objetivos = form.cleaned_data.get('objetivos')
            gym_profile.dias_treino = form.cleaned_data.get('dias_treino')
            gym_profile.save()  
        except GymProfile.DoesNotExist:
            gym_profile = form.save()

        return super().form_valid(form)

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

def home(request):
    if request.user.is_authenticated:
        gym_profile = GymProfile.objects.filter(user=request.user).first()
    else:
        gym_profile = None
    
    return render(request, 'gym/home.html', {'gym_profile': gym_profile})
