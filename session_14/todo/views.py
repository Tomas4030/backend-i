from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.views.generic import  ListView, TemplateView, FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user, logout
from django.contrib.auth.forms import UserCreationForm

from todo.forms import TasksForm
from todo.models import Task

# def index(request):
#     tasks = Task.objects.all()
#     return render(request,"todo/index.html", {"foo": "cenas", "tasks": tasks})

class TaskListView(LoginRequiredMixin, CreateView):
    login_url = "/signin"
    success_url = "/tasks"
    form_class = TasksForm
    template_name = "todo/task_list.html"

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Task.objects.filter(user=self.request.user).all()
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class IndexView(TemplateView):
    http_method_names = ['get']
    template_name = "todo/index.html"

class SingUpView(FormView):
    template_name = "registration/singup.html"
    success_url = "/signin"
    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")