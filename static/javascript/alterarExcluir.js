//função para pegar cookie do csrf_token
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function linkMudança(event, url, acao, id) {
    event.preventDefault();

    if (acao === 'Alterar') {

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