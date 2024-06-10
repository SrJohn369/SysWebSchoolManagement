import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseNotAllowed, JsonResponse

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
                'id': docente.id,
                'nome': docente.first_name + ' ' + docente.last_name,
                'cpf': docente.cpf,
                'data_nascimento': docente.data_nasc.strftime('%d/%m/%Y')
            } for docente in Docentes
        ]
        # print(docente_data)
        
        return render(request, 'baseListagem.html', {'data_static': data_static,
                                                     'data_cadastros': docente_data})
        
    
@login_required(login_url='loginInicio:login_usuario')
def cadDocente(request):
    if request.method == 'GET':
        return render(request, 'cadDocente.html', {'submit':'Cadastrar',
                                                   'titulo':'Cadastro Docente'})
    if request.method == 'POST':
        # data
        data = json.loads(request.body)
        # catch data
        nome = data.get('usuario')
        senha = data.get('senha')
        cpf = data.get('cpf')
        email = data.get('email')
        date = data.get('data_nascimento')
        names = nome.split()
        username = names[0] + str(randint(99,99999))
        # verifica se ja existe
        if Docente.objects.filter(username=username).exists():
            username = nome + str(randint(99,99999))
        # cria um obj
        cadastrar = Docente.objects.create_user(
            username=username, password=senha, first_name=names[0],
            cpf=cpf, email=email, data_nasc=date, id=randint(9999999,99999999999),
            last_name=names[-1] if len(names) > 1 else ''
        )
        # data para JsonResponse
        data = {
            'mensagem': 'Salvo com sucesso!',
            'user': f'{username}'
        }
        # salva
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
def excluirDocente(request, id):
    if request.method == "DELETE":
        docente = get_object_or_404(Docente, id=id)
        docente.delete()
        return JsonResponse({'mensagem': 'Excluido com sucesso'})
    return HttpResponseNotAllowed(['DELETE'])