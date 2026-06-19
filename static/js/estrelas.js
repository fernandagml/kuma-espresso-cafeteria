document.addEventListener("DOMContentLoaded", function () {
    const labels = document.querySelectorAll(".star-rating-input .star-icon");

    labels.forEach((label, index) => {
        label.addEventListener("click", () => {
            // Limpa o estado de todas as estrelas primeiro
            labels.forEach((l) => {
                l.textContent = "☆";
                l.classList.remove("selected");
            });

            // Preenche a estrela clicada e todas as anteriores a ela
            for (let i = 0; i <= index; i++) {
                labels[i].textContent = "★";
                labels[i].classList.add("selected");
            }
        });
    });
});