from django.urls import path
from . import views
from core.views import showAnkieta, editAnkieta, deleteResult

urlpatterns = [
    path('ankieta/<int:pk>', editAnkieta, name='edit-ankieta'),
    path('delete-result/<int:pk>', deleteResult, name='delete-result'),
    path('ankieta/', showAnkieta, name='ankieta'),
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
    path("kolejka/", views.kolejka, name="kolejka"),
    path("regulamin/", views.regulation, name="regulation"),
    path("usun-regulamin/<int:pk>", views.deleteregulation, name="deleteregulation"),
    path("edytuj-regulamin/<int:pk>", views.editregulation, name="editregulation"),
    path("edit-vote/<int:pk>", views.editVote, name="edit-votes"),
    path("edit-profile/<int:pk>", views.setting_profile, name='settings-profile'),
]
