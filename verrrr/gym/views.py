from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from gym.forms import UserProfileForm
from gym.models import UserProfile
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# View para listar as tarefas

@login_required
def profile_view(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = None
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    
    return render(request, 'profile.html', {'form': form})

# Página inicial do site
class IndexView(TemplateView):
    template_name = "gym/index.html"

# View para registro de usuário
class SignUpView(FormView):
    template_name = "registration/signup.html"
    success_url = "/login"
    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# Função para fazer logout
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
