from django.urls import path
from aluno.views import *


app_name = 'aluno'

urlpatterns = [
    path('', aluno, name='aluno'),
    path('cadastro_aluno/', cadAluno, name='cadAluno'),
    path('alter_aluno/', altAluno, name='altAluno'),
    path('excluir_aluno/', excluirAluno, name='excluirAluno'),
]
