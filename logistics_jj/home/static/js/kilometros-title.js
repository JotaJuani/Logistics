document.addEventListener("DOMContentLoaded", function () {
    const titulo = document.getElementById("titulo");
    const totalKilometros = 500000; // Cambia esto al número que quieras alcanzar
    const duracion = 4000; // Duración total del efecto en milisegundos
    const incremento = totalKilometros / (duracion / 30); // Velocidad de incremento
    let kilometrosActuales = 300000;

    const actualizarKilometros = () => {
        kilometrosActuales += incremento;

        if (kilometrosActuales >= totalKilometros) {
            kilometrosActuales = totalKilometros; // Evita que supere el límite
            titulo.innerHTML = `Durante este 2024 hemos recorrido <strong>${Math.round(kilometrosActuales)}</strong> Kilómetros!`;
            clearInterval(intervalo); // Detén la animación
        } else {
            titulo.innerHTML = `Durante este 2024 hemos recorrido <strong>${Math.round(kilometrosActuales)}</strong> Kilómetros!`;
        }
    };

    const intervalo = setInterval(actualizarKilometros, 50); // Actualiza cada 50ms
});