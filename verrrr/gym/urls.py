from django.urls import path
from django.contrib.auth.views import LoginView
from gym import views
from .views import profile_view

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("login", LoginView.as_view(), name="login"),
    path("logout", views.logout_view, name="logout"),
    path("", views.IndexView.as_view(), name="index"),
]
