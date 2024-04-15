//função para pegar cookie do csrf_token
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function gerarSenha() {
    let caracteres = 'qwertyui8WEITORAKSJDHFGNVMCZXNZ5422570cmakxafsiz@#$'; //apenas para testes não usaria isso em produção
    let senha = ''

    for (let i = 0; i < 8; i++) {
        let index = Math.floor(Math.random() * caracteres.length);
        senha += caracteres.charAt(index);
    }

    document.getElementById('gerar_senha').innerText = senha;
    document.getElementById('gerar_senha').style.display = 'block';
    document.getElementById('aviso_gerePass').style.display = 'none';
}

function voltarConfirm() {
    window.location.href = '/docente/';
}


document.getElementById('submit').addEventListener('click', async (event) => {
    event.preventDefault()
    let csrf_token = getCookie('csrftoken');

    let nomeCad = document.getElementById('nomeCad').value;
    let cpfCad = document.getElementById('cpfCad').value;
    let dateCad = document.getElementById('dateCad').value;
    let emailCad = document.getElementById('emailCad').value;
    let senhaCad = document.getElementById('gerar_senha').innerHTML;
    let carregamento = document.getElementById('carregamento');
    
    const url = `/docente/cadastro_docente/`;
    let dados = {
        method: 'POST',
        headers: {'X-CSRFToken': csrf_token},
        body: JSON.stringify({
            'usuario': nomeCad,
            'senha': senhaCad,
            'cpf': cpfCad,
            'data_nascimento': dateCad,
            'email': emailCad
        })
    }
    if (senhaCad != '') {
        carregamento.style.display = 'flex';
        await fetch(url, dados)
        .then((response) => {
            if (response.status === 201) {
                carregamento.style.display = 'none';
                document.getElementById('cadSuccessfully').style.display = 'flex';
                return response.json();
            }else if (response.status === 500) {
                document.getElementById('carregamento').style.display = 'none';
            }
        })
        .then((data) => {
            document.getElementById('dados_user_nameUser').innerHTML = 'Usuário: '  + data.user;
            document.getElementById('dados_user_pass').innerHTML = 'Senha: ' + senhaCad;
        })
        .catch((error) => {
            document.getElementById('carregamento').style.display = 'none';
            console.log('Ocorreu um erro:', error);
        });
    } else {
        document.getElementById('aviso_gerePass').style.display = 'flex';
    }
});
