import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render, get_object_or_404
from direcao.models import Direcao


@login_required(login_url='loginInicio:login_usuario')
def direcao(request):
    if request.method == 'GET':
        
        data_static = {
            'css': '/css/baseListagem.css',
            'js': 'javascript/direcaoListar.js',
            'titulo': 'Direção',
            'link': 'loginInicio:cadDirecao',
            'th_tabela': ['Nome', 'CPF', 'Data de Nascimento', 'Opções'],
            'td_links': {
                'Alterar':'direcao:altDirecao',
                'Excluir':'direcao:excluirDirecao'
            }
        }
        
        Diretores = Direcao.objects.all()
        direcao_data = [
            {
            'id': direcao.id,
            'nome': direcao.first_name + ' ' + direcao.last_name,
            'cpf': direcao.cpf,
            'data_nascimento': direcao.data_nasc.strftime('%d/%m/%Y')
            } for direcao in Diretores
        ]
        
        return render(request, 'baseListagem.html', {'data_static': data_static,
                                                     'data_cadastros': direcao_data})
    

@login_required(login_url='loginInicio:login')
def altDirecao(request, id):
    if request.method == "PUT":
        dados = json.loads(request.body)
        
        nome = dados.get('nome')
        sep_nome = nome.split()
        data_nasc = dados.get('data_nascimento')
        first_name = sep_nome[0]
        last_name = sep_nome[1] if len(sep_nome) > 1 else ''
        
        direcao = Direcao.objects.get(id=id)
        direcao.data_nasc = data_nasc
        direcao.first_name = first_name
        direcao.last_name = last_name

        try:
            direcao.save()
            return JsonResponse(data={'mensagem': 'Atuaalizado'}, status=204)
        except:
            return JsonResponse(data={'mensagem': 'Erro interno ao salvar'}, status=500)
        
        
@login_required(login_url='loginInicio:login')
def excluirDirecao(request, id):
    if request.method == "DELETE":
        direcao = get_object_or_404(Direcao, id=id)
        direcao.delete()
        return JsonResponse({'mensagem': 'Excluido com sucesso'})
    return HttpResponseNotAllowed(['DELETE'])