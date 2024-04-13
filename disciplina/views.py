from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def disciplina(request):
    if request.method == 'GET':
        data_static = {
            'css': '/css/baseListagem.css',
            'js': 'javascript/direcaoListar.js',
            'titulo': 'Disciplina',
            'link': 'disciplina:cadDisciplina',
            'th_tabela': ['Nome da Disciplina', 'Data de Criação', 'Opções'],
            'td_links': ['Alterar', 'Excluir']
        }
        return render(request, 'baseListagem.html', {'data_static': data_static})
    

# @login_required(login_url='loginInicio:login')
def cadDisciplina(request):
    if request.method == 'GET':
        return render(request, 'cadDisciplina.html')