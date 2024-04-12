from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('loginInicio.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('aluno/', include('aluno.urls')),
    path('direcao/', include('direcao.urls')),
    path('disciplina/', include('disciplina.urls')),
    path('docente/', include('docente.urls')),
    path('turma/', include('turma.urls')),
]
