const cards = document.querySelectorAll('.product-card');
const nextBtn = document.querySelector('.next-btn');
const prevBtn = document.querySelector('.prev-btn');

let currentIndex = 0;

function showNextProduct() {
  const currentCard = cards[currentIndex];
  
  currentCard.classList.remove('active');
  currentCard.classList.add('exit-next');
  
  setTimeout(() => {
    currentCard.classList.remove('exit-next');
  }, 1200);

  currentIndex = (currentIndex + 1) % cards.length;
  const nextCard = cards[currentIndex];

  nextCard.classList.add('enter-next');

  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      nextCard.classList.remove('enter-next');
      nextCard.classList.add('active');
    });
  });
}

function showPrevProduct() {
  const currentCard = cards[currentIndex];
  
  currentCard.classList.remove('active');
  currentCard.classList.add('exit-prev');
  
  setTimeout(() => {
    currentCard.classList.remove('exit-prev');
  }, 1200);

  currentIndex = (currentIndex - 1 + cards.length) % cards.length;
  const prevCard = cards[currentIndex];

  prevCard.classList.add('enter-prev');

  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      prevCard.classList.remove('enter-prev');
      prevCard.classList.add('active');
    });
  });
}

nextBtn.addEventListener('click', showNextProduct);
prevBtn.addEventListener('click', showPrevProduct);