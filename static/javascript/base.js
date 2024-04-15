// Pega referências aos elementos
let modalDocente = document.getElementById('myModalDocente');
let modalAluno = document.getElementById('myModalAluno');
let btnDocente = document.getElementById('openModalDocente');
let btnAluno = document.getElementById('openModalAluno');
let span = document.getElementsByClassName("close")[0];

// Define ação de clique para abrir o modal
btnDocente.onclick = function() {
  modal.style.display = "block";
}
btnAluno.onclick = function() {
  modal.style.display = "block";
}

// Define ação de clique para fechar o modal
span.onclick = function() {
  modal.style.display = "none";
}

// Fecha o modal se clicar fora dele
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
