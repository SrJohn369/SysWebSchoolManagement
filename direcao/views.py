from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def direcao(request):
    if request.method == 'GET':
        
        data_static = {
            'css': '/css/baseListagem.css',
            'js': 'javascript/direcaoListar.js',
            'titulo': 'Direção',
            'link': 'loginInicio:cadDirecao',
            'th_tabela': ['Nome', 'CPF', 'Data de Nascimento', 'Opções'],
            'td_links': ['Alterar', 'Excluir']
        }
        return render(request, 'baseListagem.html', {'data_static': data_static})
    

# @login_required(login_url='loginInicio:login')
def alterar(request):
    if request.method == 'GET':
        return render(request, 'alterar.html')