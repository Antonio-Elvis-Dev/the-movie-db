from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password

from .models import User
# Create your views here.

def create_user_view(request):
    
    hash_password = make_password(request.user.password)

    name = request.user.username,
    email = request.user.email,
    password = hash_password
    

    User.objects.create(name = name, email = email, password = hash_password)

    return render(request, 'cadastro/index.html')