import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse

from docente.models import Docente
from random import randint


@login_required(login_url='loginInicio:login_usuario')
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
        Docentes = Docente.objects.all()
        docente_data = [
            {
            'nome': docente.first_name + ' ' + docente.last_name,
            'cpf': docente.cpf,
            'data_nascimento': docente.data_nasc.strftime('%d/%m/%Y')
            } for docente in Docentes
        ]
        # print(alunos_data)
        
        return render(request, 'baseListagem.html', {'data_static': data_static,
                                                     'data_cadastros': docente_data})
        
    
@login_required(login_url='loginInicio:login_usuario')
def cadDocente(request):
    if request.method == 'GET':
        return render(request, 'cadDocente.html', {'submit':'Cadastrar',
                                                   'titulo':'Cadastro Docente'})
    if request.method == 'POST':
        data = json.loads(request.body)
        nome = data.get('usuario')
        senha = data.get('senha')
        cpf = data.get('cpf')
        email = data.get('email')
        date = data.get('data_nascimento')
        first_name = nome.split()
        username = first_name[0] + str(randint(99,99999))

        if Docente.objects.filter(username=username).exists():
            username = nome + str(randint(99,99999))

        cadastrar = Docente.objects.create_user(
            username=username, password=senha, first_name=first_name[0],
            cpf=cpf, email=email, data_nasc=date
        )
        
        data = {
            'mensagem': 'Salvo com sucesso!',
            'user': f'{username}'
        }
        
        try:
            cadastrar.save()
            return JsonResponse(data=data, status=201)
        except:
            return JsonResponse(data={'mensagem': 'Erro ao salvar'}, status=500)
    
    
@login_required(login_url='loginInicio:login_usuario')
def altDocente(request):
    if request.method == 'GET':
        return render(request, 'cadDocente.html', {{'submit':'Alterar',
                                                   'titulo':'Alterar Docente'}})
    

@login_required(login_url='loginInicio:login_usuario')
def excluirDocente(request):
    pass