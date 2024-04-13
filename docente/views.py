from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def docente(request):
    if request.method == 'GET':
        data_static = {
            'css': '/css/baseListagem.css',
            'js': 'javascript/docenteListar.js',
            'titulo': 'Docente',
            'link': 'docente:cadDocente',
            'th_tabela': ['Nome', 'CPF', 'Data de Nascimento', 'Opções'],
            'td_links': {
                'Alterar':'docente:altDocente',
                'Excluir':'docente:excluirDocente'
            }
        }
        return render(request, 'baseListagem.html', {'data_static': data_static})
    
    
def cadDocente(request):
    if request.method == 'GET':
        return render(request, 'cadDocente.html', {'submit':'Cadastrar',
                                                   'titulo':'Cadastro Docente'})
    

def altDocente(request):
    if request.method == 'GET':
        return render(request, 'cadDocente.html', {{'submit':'Alterar',
                                                   'titulo':'Alterar Docente'}})
    
    
def excluirDocente(request):
    pass