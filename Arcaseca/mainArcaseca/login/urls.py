from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="login"),
    path("idiot/", views.idiot, name="idiot")
]