from django.urls import path
from . import views

urlpatterns = [
    path('', views.info, name='info'),
    path('edit/<int:pk>', views.editInfo, name='editinfo'),
    path('delete/<int:pk>', views.deleteInfo, name='deleteinfo'),
    path('add/<str:pk>', views.addComment, name='comment'),
    path('delete-comment/<str:pk>', views.removeComment, name='rm-comment'),
]
