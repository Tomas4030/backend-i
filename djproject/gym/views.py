from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from gym.forms import TaskForm, UserProfileForm
from django.shortcuts import render
from gym.models import Task, UserProfile
from django.views.generic import UpdateView
from django.urls import reverse_lazy


# Create your views here.

# View para listar as tarefas
class TaskListView(LoginRequiredMixin, CreateView):
    login_url = "/signin"
    success_url = "/tasks"
    form_class = TaskForm
    template_name = "gym/task_list.html"

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Task.objects.filter(user=self.request.user).all()
        return super().get_context_data(**kwargs)    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserProfileView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "gym/user_profile.html"
    success_url = reverse_lazy("profile")

    def get_object(self, queryset=None):
        return UserProfile.objects.get_or_create(user=self.request.user)[0]

# Página inicial do site
class IndexView(TemplateView):
    template_name = "gym/index.html"

# View para registro de usuário
class SignUpView(FormView):
    template_name = "registration/signup.html"
    success_url = "/signin.html"
    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# Função para fazer logout
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
