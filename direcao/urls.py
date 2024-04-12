from django.urls import path
from direcao.views import *


app_name = 'direcao'

urlpatterns = [
    path('', direcao, name='direcao'),
    path("alterar/", alterar, name="alterar")
]
