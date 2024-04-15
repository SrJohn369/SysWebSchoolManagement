from django.db import models
from django.contrib.auth.models import User
from turma.models import Turma


class Docente(User):
    
    cpf = models.CharField(max_length=14, primary_key=True)
    data_nasc = models.DateTimeField()
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.username}'
    
    class Meta:
        verbose_name = 'Docente'