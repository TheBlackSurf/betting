from django.urls import path
from . import views

urlpatterns = [
    path('', views.info, name='info'),
    path('edit/<int:pk>', views.editInfo, name='editinfo'),
    path('delete/<int:pk>', views.deleteInfo, name='deleteinfo'),
]
