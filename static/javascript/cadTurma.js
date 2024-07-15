// Pega referências aos elementos
let modalDocente = document.getElementById('myModalDocente');
let modalAluno = document.getElementById('myModalAluno');
let btnDocente = document.getElementById('openModalDocente');
let btnAluno = document.getElementById('openModalAluno');
let btnSairAluno = document.getElementById('btn_sair_aluno');
let btnSairDocente = document.getElementById('btn_sair_docente');

// Define ação de clique para abrir o modal
btnDocente.onclick = () => {
  modalDocente.style.display = "flex";
}
btnAluno.onclick = () => {
  modalAluno.style.display = "flex";
}

// Define ação de clique para fechar o modal
btnSairAluno.onclick = () => {
  modalAluno.style.display = "none";
}
btnSairDocente.onclick = () => {
  modalDocente.style.display = "none";
}

function debug(vars) {
    Object.entries(vars).forEach(([name, value]) => {
        console.log(`${name}:`, value);
    });
}

console.log("Iniciado");
document.getElementById('submit_btn').addEventListener('click', (event) => {
	
  	event.preventDefault();

	// Coleta os dados do formulário
    const nome = document.getElementById('nomeCad').value;
    const ano = document.querySelector('input[name="Ano"]').value;
    const dataNascimento = document.getElementById('dateCad').value;
	debug({nome, ano, dataNascimento});

    // Coleta os checkboxes de docentes e disciplinas
    const docentesCheckboxes = document.querySelectorAll('input[type="checkbox"][name^="checkbox"]:checked');
    const docentes = Array.from(docentesCheckboxes).map(checkbox => checkbox.id);
	debug({docentesCheckboxes, docentes})

    // Coleta os checkboxes de alunos
    const alunosCheckboxes = document.querySelectorAll('input[type="checkbox"][name^="{{aluno}}"]:checked');
    const alunos = Array.from(alunosCheckboxes).map(checkbox => checkbox.id);
	debug({alunosCheckboxes, alunos})

    // Cria o JSON com os dados coletados
    const formData = {
        nome: nome,
        ano: ano,
        dataNascimento: dataNascimento,
        docentes: docentes,
        alunos: alunos
    };
	console.log(formData);

    // Envia o JSON para o back-end
    // fetch('/url-do-seu-endpoint/', {
    //     method: 'POST',
    //     headers: {
    //         'Content-Type': 'application/json',
    //         'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
    //     },
    //     body: JSON.stringify(formData)
    // })
    // .then(response => response.json())
    // .then(data => {
    //     console.log('Success:', data);
    // })
    // .catch((error) => {
    //     console.error('Error:', error);
    // });
});