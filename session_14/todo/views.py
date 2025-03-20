from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.views.generic import  ListView

from todo.models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request,"todo/index.html", {"foo": "cenas", "tasks": tasks})

class IndexView(ListView):
    model = Task