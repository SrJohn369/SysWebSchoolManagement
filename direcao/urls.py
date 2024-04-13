from django.urls import path
from direcao.views import *


app_name = 'direcao'

urlpatterns = [
    path('', direcao, name='direcao'),
    path('alter_direcao/', altDirecao, name='altDirecao'),
    path('excluir_direcao/', excluirDirecao, name='excluirDirecao'),
]
