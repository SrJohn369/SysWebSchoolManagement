// Pega referências aos elementos
let modalDocente = document.getElementById('myModalDocente');
let modalAluno = document.getElementById('myModalAluno');
let btnDocente = document.getElementById('openModalDocente');
let btnAluno = document.getElementById('openModalAluno');
let spanAluno = document.getElementById('spanAluno');
let spanDocente = document.getElementById('spanDocente');

// Define ação de clique para abrir o modal
btnDocente.onclick = () => {
  modalDocente.style.display = "flex";
}
btnAluno.onclick = () => {
  modalAluno.style.display = "flex";
}

// Define ação de clique para fechar o modal
spanAluno.onclick = () => {
  modalAluno.style.display = "none";
}
spanDocente.onclick = () => {
    modalDocente.style.display = "none";
}

