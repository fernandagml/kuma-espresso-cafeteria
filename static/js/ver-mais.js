const botao = document.querySelector('.btn-see-more');
const descricao = document.querySelector('.descricao-oculta');

botao.addEventListener("click", () => {
    // Escrita aparente (=== block), se sim vai pro none, esconde e muda o texto do botão
    if (descricao.style.display === "block") {
        descricao.style.display = "none";
        botao.textContent = "VER MAIS";
    // Caso o contrário, exibe e muda o texto do botão
    } else {
        descricao.style.display = "block";
        botao.textContent = "VER MENOS";
    }
});