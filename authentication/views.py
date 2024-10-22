from django.shortcuts import render

# Create your views here.

def create_user_view(request):
    user_data = {
        'name':request.user.username,
        'email':request.user.email,
        'password':request.user.password
    }

    return render(request, 'cadastro/index.html')