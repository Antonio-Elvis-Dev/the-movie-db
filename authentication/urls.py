from django.urls import path
 
from .api import authetication_router
from .views import create_user_view
urlpartterns = [
    path('cadastro/', create_user_view, name='cadastro'),
]

