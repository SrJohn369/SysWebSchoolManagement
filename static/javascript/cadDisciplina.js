//função para pegar cookie do csrf_token
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}


// fecha tela
function voltarConfirm() {
    document.getElementById('cadSuccessfully').style.display = 'none';
}


//cadastra turma
document.getElementById('cad_turma').addEventListener('click', async (event) => {
    // evitar reload da pagina
    event.preventDefault();
    let csrf_token = getCookie('csrftoken');

    // variaveis do formulário
    let nomeDisciplina = document.getElementById('nomeCad').value;
    let dataCadDisciplina = document.getElementById('dateCad').value;

    // dados para conexão com a endpoint
    const url = ``;
    let dados = {
        method: 'POST',
        headers: {'X-CSRFToken': csrf_token},
        body: JSON.stringify({
            'nome_diciplina': nomeDisciplina,
            'data_cad_disciplina': dataCadDisciplina
        })
    }

    // tela de carregamento
    document.getElementById('carregamento').style.display = 'flex';

    // fazendo a request POST
    await fetch(url, dados)
        // request
        .then((response) => {
            if (response.status == 201) {
                document.getElementById('carregamento').style.display = 'none';
                document.getElementById('cadSuccessfully').style.display = 'flex';

                return response.json();

            }else if (response.status === 500) {
                document.getElementById('carregamento').style.display = 'none';
                console.log('error interno');
            }
        })
        // captura erro
        .catch((error) => {
            document.getElementById('carregamento').style.display = 'none';
            console.log('Ocorreu um erro:', error);
        });

});