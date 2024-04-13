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
            'td_links': ['Alterar', 'Excluir']
        }
        return render(request, 'baseListagem.html', {'data_static': data_static})
    
    
def cadDocente(request):
    if request.method == 'GET':
        
        render(request, 'cadDocente.html')