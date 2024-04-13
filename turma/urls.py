from django.urls import path
from turma.views import *


app_name = 'turma'

urlpatterns = [
    path('', turma, name='turma'),
    path('cadastro_turma/', cadTurma, name='cadTurma'),
    path('alter_turma/', altTurma, name='altTurma'),
    path('excluir_turma/', excluirTurma, name='excluirTurma'),
    path('verDocentes_turma/', verDocentesTurma, name='verDocentesTurma'),
    path('verAlunos_turma/', verAlunosTurma, name='verAlunosTurma'),
]
