from django.urls import path
from turma.views import *


app_name = 'turma'

urlpatterns = [
    path('', turma, name='turma'),
    path('cadastro_turma/', cadTurma, name='cadTurma')
]
