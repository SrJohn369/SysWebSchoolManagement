from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def direcao(request):
    if request.method == 'GET':
        return render(request, 'direcao.html')
    

# @login_required(login_url='loginInicio:login')
def alterar(request):
    if request.method == 'GET':
        return render(request, 'alterar.html')