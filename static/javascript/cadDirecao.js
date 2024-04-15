if (isAuthenticated) {
    document.getElementById('img-drop').style.display = 'flex';
}

//função para pegar cookie do csrf_token
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function verifyPass() {
    let password = document.getElementById('senhaCad').value;
    let pwdConfirm = document.getElementById('confirmSenhaCad').value;

    if (password === pwdConfirm) {
        return true;
    } else {
        return false;
    }
}

function voltarConfirm() {
    if (isAuthenticated) {
        window.location.href = '/direcao/';
    } else {
        window.location.href = '/login/';
    }
}

document.getElementById('submit-cad').addEventListener('click', async (event) => {
    event.preventDefault()
    let csrf_token = getCookie('csrftoken');

    let nomeCad = document.getElementById('nomeCad').value;
    let cpfCad = document.getElementById('cpfCad').value;
    let dateCad = document.getElementById('dateCad').value;
    let emailCad = document.getElementById('emailCad').value;
    let senhaCad = document.getElementById('senhaCad').value;
    
    const url = `/cadastro_direcao/`;
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

    // verifica senhas
    if (verifyPass()) {
        document.getElementById('carregamento').style.display = 'flex';
        await fetch(url, dados)
        .then((response) => {
            if (response.status === 201) {
                console.log('verificado code 201');
                document.getElementById('carregamento').style.display = 'none';
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
        document.getElementById('senhasIncorretas').style.display = 'block';
    }
});
