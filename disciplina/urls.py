from django.urls import path
from disciplina.views import *


app_name = 'disciplina'

urlpatterns = [
    path('', disciplina, name='disciplina')
]
