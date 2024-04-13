from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def turma(request):
    if request.method == 'GET':
        data_static = {
            'css': '/css/baseListagem.css',
            'js': 'javascript/direcaoListar.js',
            'titulo': 'Turma',
            'link': 'turma:cadTurma',
            'th_tabela': ['Nome da Turma', 'Ano', 'Data de Criação', 'Opções'],
            'td_links': ['Ver Docente', 'Ver Aluno','Alterar', 'Excluir']
        }
        return render(request, 'baseListagem.html', {'data_static': data_static})
    

# @login_required(login_url='loginInicio:login')
def cadTurma(request):
    if request.method == 'GET':
        return render(request, 'cadTurma.html')