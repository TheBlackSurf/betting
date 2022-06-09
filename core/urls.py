from django.urls import path
from . import views


urlpatterns = [
    path('', views.postdetail, name='dash'),
    path('all/', views.allvote, name='allvote'),
    path('vote/edit/<int:pk>', views.updatevote, name='edit-vote'),
    path('vote/add/<int:pk>', views.vote, name='edit'),
    # users
    path('user/<int:pk>', views.userdetail, name='userdetail'),
    path('users/', views.alluser, name='alluser'),
    # register login logout
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),

]

