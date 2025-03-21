from django.urls import path
from django.contrib.auth.views import LoginView
from todo import views

urlpatterns = [
    path("tasks", views.TaskListView.as_view(), name="task_list"),
    path("signup", views.SingUpView.as_view(), name="signup"),
    path("signin", LoginView.as_view(), name="signin"),
    path("", views.IndexView.as_view(), name="index")
]