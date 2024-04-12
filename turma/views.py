from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def turma(request):
    if request.method == 'GET':
        return render(request, 'turma.html')