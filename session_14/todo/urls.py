from django.urls import include,path
from todo import views

urlpatterns = [

    path("", views.IndexView.as_view(), name="index")
]