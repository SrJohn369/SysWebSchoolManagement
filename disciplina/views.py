import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from random import randint

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
                'id': disciplina.id,
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
    
    if request.method == 'POST':
        data = json.loads(request.body)
        
        # Dados
        nome_diciplina = data.get("nome_diciplina")
        data_cad_disciplina = data.get("data_cad_disciplina")
        
        # Obj
        disciplina = Disciplina.objects.create(
            id=randint(9999999,99999999999),
            nome_disciplina=nome_diciplina,
            data_criacao=data_cad_disciplina
        )
        
        # Salvar disciplina
        try:
            disciplina.save()
            return JsonResponse(data={'mensagem': 'Sucesso ao criar disciplina'}, status=201)
        except:
            return JsonResponse(data={'mensagem': 'Erro ao salvar'}, status=500)
        
    
@login_required(login_url='loginInicio:login')    
def altDisciplina(request):
    if request.method == 'GET':
        return render(request, 'cadDisciplina.html', {'data_static':'Alterar'})    
    

@login_required(login_url='loginInicio:login')
def excluirDisciplina(request):
    pass