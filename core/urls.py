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

]

