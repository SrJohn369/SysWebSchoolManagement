import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed, JsonResponse
from django.shortcuts import get_object_or_404, render

from aluno.models import Aluno
from random import randint


@login_required(login_url='loginInicio:login_usuario')
def aluno(request):
    if request.method == 'GET':

        data_static = {
            'css': '/css/baseListagem.css',
            'js': 'javascript/alunoListar.js',
            'titulo': 'Aluno(a)',
            'link': 'aluno:cadAluno',
            'th_tabela': ['Nome', 'CPF', 'Data de Nascimento', 'Opções'],
            'td_links': {
                'Alterar':'aluno:altAluno',
                'Excluir':'aluno:excluirAluno'
            }
        }
        
        alunos = Aluno.objects.all()
        alunos_data = [
            {
            'id': aluno.id,
            'nome': aluno.first_name + ' ' + aluno.last_name,
            'cpf': aluno.cpf,
            'data_nascimento': aluno.data_nasc.strftime('%d/%m/%Y')
            } for aluno in alunos
        ]
        # print(alunos_data)
        
        return render(request, 'baseListagem.html', {'data_static': data_static,
                                                     'data_cadastros': alunos_data})


@login_required(login_url='loginInicio:login_usuario')
def cadAluno(request):
    if request.method == 'GET':
        return render(request, 'cadAluno.html', {'titulo': 'Cadastrar Aluno(a)',
                                                 'submit': 'Cadastrar'})
    if request.method == 'POST':
        data = json.loads(request.body)
        nome = data.get('usuario')
        senha = data.get('senha')
        cpf = data.get('cpf')
        email = data.get('email')
        date = data.get('data_nascimento')
        names = nome.split()
        username = names[0] + str(randint(99,99999))

        if Aluno.objects.filter(username=username).exists():
            username = nome + str(randint(99,99999))

        cadastrar = Aluno.objects.create_user(
            username=username, password=senha, first_name=names[0],
            cpf=cpf, email=email, data_nasc=date, id=randint(9999999,99999999999),
            last_name=names[-1] if len(names) > 1 else ''
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
def altAluno(request, id):
    if request.method == "PUT":
        dados = json.loads(request.body)
        
        nome = dados.get('nome')
        sep_nome = nome.split()
        data_nasc = dados.get('data_nascimento')
        first_name = sep_nome[0]
        last_name = sep_nome[1] if len(sep_nome) > 1 else ''
        
        aluno = Aluno.objects.get(id=id)
        aluno.data_nasc = data_nasc
        aluno.first_name = first_name
        aluno.last_name = last_name

        try:
            aluno.save()
            return JsonResponse(data={'mensagem': 'Atuaalizado'}, status=204)
        except:
            return JsonResponse(data={'mensagem': 'Erro interno ao salvar'}, status=500)


@login_required(login_url='loginInicio:login_usuario')
def excluirAluno(request, id):
    if request.method == "DELETE":
        aluno = get_object_or_404(Aluno, id=id)
        aluno.delete()
        return JsonResponse({'mensagem': 'Excluido com sucesso'})
    return HttpResponseNotAllowed(['DELETE'])