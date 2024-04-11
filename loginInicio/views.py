import json

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse



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
            print('deu bom')
            return redirect('loginInicio:inicio')
        else:
            return JsonResponse({'erro': 'Usuario ou senha incorreta'}, status=404)


@csrf_protect
def cadDirecao(request):
    if request.method == 'GET':
        return render(request, 'cadDireção.html')
    

def escSenha(request):
    if request.method == 'GET':
        return render(request, 'escSenha.html')


