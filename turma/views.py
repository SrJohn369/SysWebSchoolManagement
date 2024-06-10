from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed, JsonResponse
from django.shortcuts import get_object_or_404, render

from turma.models import Turma
from docente.models import Docente
from aluno.models import Aluno
from disciplina.models import Disciplina


@login_required(login_url='loginInicio:login_usuario')
def turma(request):
    if request.method == 'GET':
        data_static = {
            'css': '/css/baseListagem.css',
            'js': 'javascript/direcaoListar.js',
            'titulo': 'Turma',
            'link': 'turma:cadTurma',
            'th_tabela': ['Nome da Turma', 'Ano', 'Data de Criação', 'Opções'],
            'td_links': {
                'Ver Docentes':'turma:verDocentesTurma', 
                'Ver Alunos':'turma:verAlunosTurma',
                'Alterar':'turma:altTurma',
                'Excluir':'turma:excluirTurma'
            }
        }
        
        turmas = Turma.objects.all()
        turmas_data = [
            {
                'id': turma.id,
                'nome_turma': turma.nome_turma,
                'data_criacao': turma.data_criacao.strftime('%d/%m/%Y'),
                'ano': turma.ano
            } for turma in turmas
        ]
        
        
        return render(request, 'baseListagem.html', {'data_static': data_static,
                                                     'data_cadastros': turmas_data})
    

@login_required(login_url='loginInicio:login')
def cadTurma(request):
    if request.method == 'GET':
        # instancias dos dados
        docentes = Docente.objects.all()
        alunos = Aluno.objects.all()
        disciplinas = Disciplina.objects.all()
        # dicionarios de dados em preformatados em json
        data_docente = [{
            'nome': docente.first_name
        }for docente in docentes]
        
        data_aluno = [{
            'nome': aluno.first_name,
            'cpf': aluno.cpf,
            'data_nasc': aluno.data_nasc.strftime("%d/%m/%Y")
        }for aluno in alunos]
        
        data_disciplina = [{
            'nome_disciplina': disciplina.nome_disciplina
        }for disciplina in disciplinas]
        
        # renderiza pagina
        return render(request, 'cadTurma.html', {'submit': 'Criar Turma',
                                                 'data_docente': data_docente,
                                                 'data_aluno': data_aluno,
                                                 'data_disciplina': data_disciplina})
    if request.method == 'POST':
        pass
    
 
# PUT   
@login_required(login_url='loginInicio:login')
def altTurma(request):
    if request.method == 'GET':
        return render(request, 'cadTurma.html', {'submit': 'Alterar Turma'})
    
    
# DELETE
@login_required(login_url='loginInicio:login')
def excluirTurma(request, id):
    if request.method == "DELETE":
        turma = get_object_or_404(Turma, id=id)
        turma.delete()
        return JsonResponse({'mensagem': 'Excluido com sucesso'})
    return HttpResponseNotAllowed(['DELETE'])


@login_required(login_url='loginInicio:login')
def verDocentesTurma(request):
    pass


@login_required(login_url='loginInicio:login')
def verAlunosTurma(request):
    pass