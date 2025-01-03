document.addEventListener("DOMContentLoaded", function () {
    const titulo = document.getElementById("titulo");
    const totalKilometros = 500000;
    const duracion = 4000; 
    const incremento = totalKilometros / (duracion / 30);
    let kilometrosActuales = 300000;

    const actualizarKilometros = () => {
        kilometrosActuales += incremento;

        if (kilometrosActuales >= totalKilometros) {
            kilometrosActuales = totalKilometros; 
            titulo.innerHTML = `Durante este 2024 hemos recorrido <strong>${Math.round(kilometrosActuales)}</strong> Kilómetros!`;
            clearInterval(intervalo); 
        } else {
            titulo.innerHTML = `Durante este 2024 hemos recorrido <strong>${Math.round(kilometrosActuales)}</strong> Kilómetros!`;
        }
    };

    const intervalo = setInterval(actualizarKilometros, 50); 
});