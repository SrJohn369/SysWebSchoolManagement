from django.db import models
from turma.models import Turma


class Disciplina(models.Model):
    
    nome_disciplina = models.CharField(max_length=50)
    data_criacao = models.DateTimeField(default='1999-01-01')
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.nome_disciplina}'
    
    class Meta:
        verbose_name = 'Disciplina'