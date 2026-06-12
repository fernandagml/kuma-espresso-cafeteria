const botao = document.querySelector('.btn-see-more');
const descricao = document.querySelector('.descricao-oculta');

botao.addEventListener("click", () => {
    if (descricao.style.display === "block") {
        descricao.style.display = "none";
        botao.textContent = "VER MAIS";
    } else {
        descricao.style.display = "block";
        botao.textContent = "VER MENOS";
    }
});