from ninja import ModelSchema, Schema
# from typing import
from .models import User as ModelUser


class UserCreateSchema(Schema):
    name:str
    email: str
    password: str
    tel: str = None 

class UserResponseSchema(ModelSchema):
    class Config:
        model = ModelUser
        model_exclude = ["password","tel"]
        # model_fields = "__all__" #indica que todos os campos do modelo ModelAlimento devem ser incluídos no esquema.


