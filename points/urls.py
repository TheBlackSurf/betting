from django.urls import path
from . import views


urlpatterns = [
    path('', views.viewpoint, name='viewpoint'),
    path('addpoints/', views.addpoints, name='addpoints'),
    path('edit-points/<int:pk>/', views.editpoints, name='editpoints'),
]
