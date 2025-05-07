let currentSlide = 0;
const totalSlides = 2; // Número de imagens

function updateSlide() {
    const transformValue = currentSlide * -50; // Move 50% a cada vez
    document.querySelector('.siteImagem').style.transform = `translateX(${transformValue}%)`;
}

// Navegação manual
document.querySelector(".arrowRight").addEventListener("click", () => {
    currentSlide = (currentSlide + 1) % totalSlides;
    updateSlide();
});

document.querySelector(".arrowLeft").addEventListener("click", () => {
    currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
    updateSlide();
});

// Troca automática a cada 1 segundo
setInterval(() => {
    currentSlide = (currentSlide + 1) % totalSlides;
    updateSlide();
}, 5000);



// oapcity transition
const carrousel = document.querySelector(".carrousel");

carrousel.addEventListener("mouseenter", ()=>{
    const arrowRight = document.querySelector(".arrowRight");
    const arrowLeft = document.querySelector(".arrowLeft");

    arrowRight.classList.add("opacityTrans");
    arrowLeft.classList.add("opacityTrans");

});

carrousel.addEventListener("mouseleave", () => {
    const arrowRight = document.querySelector(".arrowRight");
    const arrowLeft = document.querySelector(".arrowLeft");

    arrowRight.classList.remove("opacityTrans");
    arrowLeft.classList.remove("opacityTrans");
});

const botaoAdquirir = document.querySelector(".botaoAdquirir");

botaoAdquirir.addEventListener("click",()=>{
    window.open("https://wa.me/5535988874386?text=Olá%2C+tenho+interesse+no+seu+café+arábica! ");
});