from ninja import NinjaAPI
 
from authentication.api import authetication_router

from django.http import HttpRequest

api = NinjaAPI()

api.add_router("/authentication",authetication_router)
