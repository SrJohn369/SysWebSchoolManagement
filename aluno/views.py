from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def aluno(request):
    if request.method == 'GET':
    
        data_static = {
            'css': '/css/baseListagem.css',
            'js': 'javascript/alunoListar.js',
            'titulo': 'Aluno(a)',
            'link': 'aluno:cadAluno',
            'th_tabela': ['Nome', 'CPF', 'Data de Nascimento', 'Opções'],
            'td_links': ['Alterar', 'Excluir']
        }
        return render(request, 'baseListagem.html', {'data_static': data_static})
    
    
def cadAluno(request):
    if request.method == 'GET':
        
        render(request, 'cadAluno.html')