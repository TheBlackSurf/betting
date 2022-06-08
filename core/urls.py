from django.urls import path
from . import views


urlpatterns = [
    path('', views.postdetail, name='dash'),
    path('vote/edit/<int:pk>', views.updatevote, name='edit-vote'),
    path('vote/add/<int:pk>', views.vote, name='edit'),
]

