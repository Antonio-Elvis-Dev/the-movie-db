from django.urls import path
 
from .views import create_user_view

urlpatterns = [
    path('cadastro/', create_user_view, name='cadastro'),
]

