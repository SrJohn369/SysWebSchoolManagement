from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from direcao.models import Direcao


@login_required(login_url='loginInicio:login_usuario')
def direcao(request):
    if request.method == 'GET':
        
        data_static = {
            'css': '/css/baseListagem.css',
            'js': 'javascript/direcaoListar.js',
            'titulo': 'Direção',
            'link': 'loginInicio:cadDirecao',
            'th_tabela': ['Nome', 'CPF', 'Data de Nascimento', 'Opções'],
            'td_links': {
                'Alterar':'direcao:altDirecao',
                'Excluir':'direcao:excluirDirecao'
            }
        }
        
        Diretores = Direcao.objects.all()
        direcao_data = [
            {
            'nome': direcao.first_name + ' ' + direcao.last_name,
            'cpf': direcao.cpf,
            'data_nascimento': direcao.data_nasc.strftime('%d/%m/%Y')
            } for direcao in Diretores
        ]
        
        return render(request, 'baseListagem.html', {'data_static': data_static,
                                                     'data_cadastros': direcao_data})
    

@login_required(login_url='loginInicio:login')
def altDirecao(request):
    if request.method == 'GET':
        return render(request, 'alterar.html')
        
        
@login_required(login_url='loginInicio:login')
def excluirDirecao(request):
    pass