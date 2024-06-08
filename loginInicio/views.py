import json

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse

from direcao.models import Direcao

from random import randint


@login_required(login_url='loginInicio:login_usuario')
def inicio(request):
    if request.method == 'GET':
        return render(request, 'inicio.html')


@csrf_protect
def login_usuario(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        data = json.loads(request.body)
        login_usuario = data.get('usuario')
        login_senha = data.get('senha')
        user = authenticate(username=login_usuario, password=login_senha)
        
        if user is not None:
            login(request, user)
            return JsonResponse({'mensagem': 'Sucesso no login'}, status=200)
        else:
            return JsonResponse({'mensagem': 'Usuario ou senha incorreta'}, status=404)
        

@login_required(login_url='loginInicio:login_usuario')
def logout_usuario(request):
    logout(request)
    return redirect('loginInicio:login_usuario')


@csrf_protect
def cadDirecao(request):
    if request.method == 'GET':
        return render(request, 'cadDirecao.html')
    
    if request.method == 'POST':
        data = json.loads(request.body)
        nome = data.get('usuario')
        senha = data.get('senha')
        cpf = data.get('cpf')
        email = data.get('email')
        date = data.get('data_nascimento')
        names = nome.split()
        username = names[0] + str(randint(99,99999))
        
        if Direcao.objects.filter(username=username).exists():
            username = names[0] + str(randint(99,99999))
        
        cadastrar = Direcao.objects.create_user(
            username=username, password=senha, first_name=names[0],
            cpf=cpf, email=email, data_nasc=date, 
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
def escSenha(request):
    if request.method == 'GET':
        return render(request, 'escSenha.html')


