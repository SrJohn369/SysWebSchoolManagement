from direcao.models import Direcao
from rest_framework import serializers


class SerieDirecao(serializers.ModelSerializer):
    class Meta:
        model = Direcao
        fields = ['id', 'first_name', 'cpf', 'data_nasc']
        

