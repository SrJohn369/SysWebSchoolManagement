# SysWebSchoolManagement-Back
![Static Badge](https://img.shields.io/badge/status-em_desenvolvimento-blue?style=for-the-badge&labelColor=grey)
![GitHub Tag](https://img.shields.io/github/v/tag/SrJohn369/SysWebSchoolManagement?style=for-the-badge&label=Vers%C3%A3o)


## Descrição
Diretório do Sistema Web de Gerenciamento Escolar.  
Sistema é criado totalmente em Django que é de arquitetura MVT(Model View Template) sendo bem semelhante a arquitetura MVC(Model View Controller). Como são semelhantes e não idênticas resolvi adicionar uma API como bônus do projeto, usando DRF(Django Rest Framework).

## Tecnologias usadas
![python](https://img.shields.io/badge/python-%233776AB?style=for-the-badge&logo=python&logoColor=yellow)
![docker](https://img.shields.io/badge/docker-%232496ED?style=for-the-badge&logo=docker&logoColor=black)
![git](https://img.shields.io/badge/git-%23F05032?style=for-the-badge&logo=git&logoColor=black)
[<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/djangorest/djangorest-line.svg" style="width:44px; height:44px"/>](https://www.django-rest-framework.org/)
![django](https://img.shields.io/badge/django-%23092E20?style=for-the-badge&logo=django)
![postgresql](https://img.shields.io/badge/postgresql-%234169E1?style=for-the-badge&logo=postgresql&logoColor=%23fff)
![Static Badge](https://img.shields.io/badge/javascript-%23F7DF1E?style=for-the-badge&logo=javascript&logoColor=%23000)
![Static Badge](https://img.shields.io/badge/html5-%23E34F26?style=for-the-badge&logo=html5&logoColor=%23fff)
![Static Badge](https://img.shields.io/badge/css3-%231572B6?style=for-the-badge&logo=css3&logoColor=%23fff)
![Static Badge](https://img.shields.io/badge/supabase-%233FCF8E?style=for-the-badge&logo=supabase&logoColor=%23fff)

## Endpoints da API 
##### https://syswebschoolmanagement.onrender.com/api/docentes Docentes API
Este endpoint retorná todos os docentes cadastrados com os dados:
- nome
- cpf
- data de nascimento
##### https://syswebschoolmanagement.onrender.com/api/alunos Aluno API
Este endpoint retorná todos os docentes cadastrados com os dados:
- nome
- cpf
- data de nascimento
##### https://syswebschoolmanagement.onrender.com/api/diretores Direcao API
Este endpoint retorná todos os docentes cadastrados com os dados:
- nome
- cpf
- data de nascimento
## Como usar a aplicação na sua máquina
### Para usar o sistema na sua máquina siga os seguintes passos
1. Baixe o repositório na sua máquina clicando [aqui](https://github.com/SrJohn369/SysWebSchoolManagement/archive/refs/heads/main.zip)  

2. Crie um ambiente de desenvolvimento python. Você pode rodar o comando ```python -m venv venv``` no seu 
terminal para criar um ambiente virtual.
3. Ative seu ambiente virtual. Pelo Windows basta usar ```venv\Scripts\activate```
4. Crie um arquivo de variáveis de ambiente `.env` e coloque as variáveis `URLDATABASE` com a url do seu banco de dados e uma `SECRET_KEY` para Django.
5. Rode o comando `pip intall -r requirements.txt` para instalar as dependências.
6. Rode o comando `python manager.py runserver` para rodar o servidor e iniciar a aplicação.
7. Faça bom uso :smile: .
## Versão atual 
![GitHub Tag](https://img.shields.io/github/v/tag/SrJohn369/SysWebSchoolManagement?style=for-the-badge&label=Vers%C3%A3o)  

### Ações possíveis:
1. Cadastrar, fazer login e logout da Direção 
2. Cadastrar Alunos, Docentes e outros Diretores
3. Visualizar Alunos, Docentes, Turmas, Disciplinas e Diretores cadastrados

### Versões futuras:
##### Ações possíveis:
- v1.16.27:  
- - Cadastrar Turma
- - Telas Vincular Docente, Disciplina e Alunos
- - Vincular Docente, Disciplina e Alunos
- v1.18.28:
- - Pesquisar Nome
- v1.18.29:
- - Redefinir Senha da direção via email
- v1.20.29:
- - Tela Detalhar Docente e Aluno
- v1.20.32:
- - Alterar Aluno, Turma, Disciplina, Docente, Direção
- v1.20.35:
- - Deletar Aluno, Turma, Disciplina, Docente, Direção
- v1.21.36:
- - Tela Gerar boletim
- - Função Gerar boletim
## Desenvolvedor
| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/106630200?v=4" width=115><br><sub>João Victor</sub>](https://github.com/SrJohn369) | 
| :---: |