from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from disciplina.models import Disciplina


@login_required(login_url='loginInicio:login_usuario')
def disciplina(request):
    if request.method == 'GET':
        data_static = {
            'css': '/css/baseListagem.css',
            'js': 'javascript/direcaoListar.js',
            'titulo': 'Disciplina',
            'link': 'disciplina:cadDisciplina',
            'th_tabela': ['Nome da Disciplina', 'Data de Criação', 'Opções'],
            'td_links': {
                'Alterar':'disciplina:altDisciplina',
                'Excluir':'disciplina:excluirDisciplina'
            }
        }
        
        disciplinas = Disciplina.objects.all()
        disciplinas_data = [
            {
            'nome_disciplina': disciplina.nome_disciplina,
            'data_criacao': disciplina.data_criacao.strftime('%d/%m/%Y')
            } for disciplina in disciplinas
        ]
        
        
        return render(request, 'baseListagem.html', {'data_static': data_static,
                                                     'data_cadastros': disciplinas_data})
    

@login_required(login_url='loginInicio:login')
def cadDisciplina(request):
    if request.method == 'GET':
        return render(request, 'cadDisciplina.html', {'data_static':'Criar'})
    

@login_required(login_url='loginInicio:login')    
def altDisciplina(request):
    if request.method == 'GET':
        return render(request, 'cadDisciplina.html', {'data_static':'Alterar'})    
    

@login_required(login_url='loginInicio:login')
def excluirDisciplina(request):
    pass