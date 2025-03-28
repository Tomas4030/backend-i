from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # Página inicial
    path('home/', views.home, name='home'),  # Página inicial do usuário após login
    path('signup/', views.SignUpView.as_view(), name='signup'),  # Cadastro
    path('login/', views.CustomLoginView.as_view(), name='login'),  # Login
    path('logout/', views.logout_view, name='logout'),  # Logout
    path('gym_profile_form/', views.GymProfileCreateView.as_view(), name='gym_profile_form'),  # Formulário de perfil
]
