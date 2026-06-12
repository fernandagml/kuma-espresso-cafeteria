const stars = [
    document.getElementById('star1'),
    document.getElementById('star2'),
    document.getElementById('star3'),
    document.getElementById('star4'),
    document.getElementById('star5')
];
const inputComentario = document.querySelector('#comentario');
const buttonAvaliacao = document.querySelector('#buttonAvaliacao');

function avaliar() {
    const starSelecionada = stars.find(star => star && star.checked);
    const avaliacao = starSelecionada.value;

    if (starSelecionada) {
        fetch('/comentario/post/<id_produto>', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "avaliacao": parseInt(avaliacao)
            })
        }).then(response => {
            if (response.ok) {
                window.location.reload();
            }
        });
    };
};

buttonAvaliacao.addEventListener('click', avaliar);