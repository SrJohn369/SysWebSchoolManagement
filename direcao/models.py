from django.contrib.auth.models import User
from django.db import models


class Direcao(User):
    
    cpf = models.CharField(max_length=14, primary_key=True)
    data_nasc = models.DateTimeField()
    
    def __str__(self) -> str:
        return f'{self.username}'
    
    class Meta:
        verbose_name = 'Diretio(a)'

