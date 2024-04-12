from django.urls import path
from aluno.views import *


app_name = 'aluno'

urlpatterns = [
    path('', aluno, name='aluno')
]
