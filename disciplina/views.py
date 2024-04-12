from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def disciplina(request):
    if request.method == 'GET':
        return render(request, 'disciplina.html')