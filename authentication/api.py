from ninja import Router

from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password

from django.http import JsonResponse

from .schemas import UserCreateSchema, UserResponseSchema
from .models import User as ModelUser

authetication_router = Router()

@authetication_router.post('create_user',response=UserResponseSchema)
def create_user(request,user_data:UserCreateSchema ):

    hashed_password = make_password(user_data.password)

    user = ModelUser.objects.create(
        name= user_data.name,
        email= user_data.email,
        password= hashed_password
    )

    return user