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

