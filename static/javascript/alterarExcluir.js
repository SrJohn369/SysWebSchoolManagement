//função para pegar cookie do csrf_token
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}


function linkMudança(event, url, acao, id) {
    event.preventDefault();
    // PEGANDO ELEMENTOS
    let row = document.getElementById(`${id}`);
    let colunas = row.querySelectorAll('td');
    let titulos = document.querySelectorAll('th');
    // GARANTINDO BOM FUNCIONAMENTO DA EDIÇÃO
    let dadosJson = {};
    let vOriginals = [];
    let links = '';
    //==================================================================
    // FUNÇÕES DOS BTN
    function salvarDados() {
        let csrf_token = getCookie('csrftoken');
        // aplicando valores nas colunas
        colunas.forEach((coluna, i) => {
            const inputToTxt = coluna.querySelector('input');
            if (i !== colunas.length - 1) {
                coluna.innerHTML = inputToTxt.value;
            } else {
                coluna.innerHTML = links;
            }
        });

        // verifica qual tipo de tabela de exibição
        if (titulos[0].textContent === 'Nome') {
            dadosJson = {
                'nome': colunas[0].textContent,
                'data_nascimento': colunas[2].textContent
            };
        } else if (titulos[0].textContent === 'Nome da Disciplina') {
            dadosJson = {
                'nome_diciplina': colunas[0].textContent,
                'data_cad_disciplina': colunas[1].textContent
            };
        } else if (titulos[0].textContent === 'Nome da Turma') {
            dadosJson = {
                'nome_turma': colunas[0].textContent,
                'ano': colunas[1].textContent,
                'data_criação': colunas[2].textContent
            };
        }
        // criando request
        let dados = {
            method: 'PUT',
            headers: {'X-CSRFToken': csrf_token},
            body: JSON.stringify(dadosJson)
        };
        // REQUEST PUT
        fetch(url, dados)
        .then(response => {
            if (response.status === 204) {
                console.log("Atualizado com sucesso!");
            } else {
                console.log("DEU RUIM");
            }
        })
    }
    // restaura valores nas colunas
    function cancelarAlteracao() {
        colunas.forEach((coluna, i) => {
            if (i !== colunas.length - 1) {
                coluna.innerHTML = vOriginals[i];
            } else {
                coluna.innerHTML = links;
            }
        });
    }
    //==================================================================
    // MODIFICAÇÕES DOS LINKS & EXCLUSÃO DE LINHA
    if (acao === 'Alterar') {
        colunas.forEach((coluna, index) => {
            if (index !== colunas.length -1) {
                vOriginals.push(coluna.innerText); // salva dados atuais

                const valorAntigo = coluna.innerText; 
                const input = document.createElement('input');
                // verifica se é data
                if (coluna.textContent.includes('/')) {
                    input.type = 'date';
                    let [d, m, a] = valorAntigo.split('/');
                    input.value = `${a}-${m}-${d}`;
                } else if (coluna.textContent.includes('.')) {
                    input.type = 'text';
                    input.id = 'cpf_input';
                    input.maxLength = '14';
                    input.value = valorAntigo;
                    input.setAttribute("readOnly", "true")
                } else {
                    input.type = 'text';
                    input.value = valorAntigo;
                    console.log(titulos[1].textContent, index);
                }

                coluna.innerHTML = ''; // Limpa o conteúdo da célula
                coluna.appendChild(input); // Adiciona o input na célula
            } else {
                links = coluna.innerHTML; // salva os links
                vOriginals.push(links);
                const btnSalvar = document.createElement('button');
                const btnCancelar = document.createElement('button');
                btnSalvar.textContent = 'Salvar';
                btnCancelar.textContent = 'Cancelar';

                btnSalvar.onclick = salvarDados;
                btnCancelar.onclick = cancelarAlteracao;

                coluna.innerHTML = '';
                coluna.appendChild(btnSalvar);
                coluna.appendChild(btnCancelar);
            }
        });
    } else if (acao === 'Excluir') {
        let csrf_token = getCookie('csrftoken');

        let dados = {
            method: 'DELETE',
            headers: {'X-CSRFToken': csrf_token}
        }

        fetch(url, dados)
        .then((response) => {
            if (response.status === 200){
                document.getElementById(`${id}`).remove();
            }
        })
    }
}