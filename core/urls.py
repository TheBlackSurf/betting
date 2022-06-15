from django.urls import path
from . import views


urlpatterns = [
    path("addpost/", views.addpost, name="addpost"),
    path("addkolejka/", views.addkolejka, name="addkolejka"),
    path("deletepost/<int:pk>", views.deletepost, name="deletepost"),
    path("deletevote/<int:pk>", views.deletevote, name="deletevote"),
    path("", views.postdetail, name="dash"),
    path("all/", views.allvote, name="allvote"),
    path("vote/edit/<int:pk>", views.updatevote, name="edit-vote"),
    path("vote/add/<int:pk>", views.addvote, name="edit"),
    path("user/<int:pk>", views.userdetail, name="userdetail"),
    path("users/", views.alluser, name="alluser"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("kolejka/", views.kolejka, name="kolejka")
]
