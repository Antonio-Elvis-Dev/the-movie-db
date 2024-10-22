from django.urls import path

from authentication.urls import create_user_view

urlpartterns = [
    path('', create_user_view, name='cadastro'),
]

