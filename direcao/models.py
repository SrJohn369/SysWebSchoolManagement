from django.contrib.auth.models import User
from django.db import models


class Direcao(User):
    
    cpf = models.CharField(max_length=11)
    data_nasc = models.DateField()
    
    def __str__(self) -> str:
        return f'{self.first_name}'
    
    class Meta:
        verbose_name = 'Diretion'

