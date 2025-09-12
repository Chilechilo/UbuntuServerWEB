window.addEventListener("DOMContentLoaded", () => {
    alert("Bienvenidos a mi pagina");

    const COUNTER_KEY = "visitas_mi_pagina";

    const visitasActuales = Number(localStorage.getItem(COUNTER_KEY) || 0);
    const nuevasVisitas = visitasActuales + 1;
    localStorage.setItem(COUNTER_KEY, String(nuevasVisitas));

    const contadorEl = document.getElementById("contador-visitas");
    if (contadorEl) {
        contadorEl.textContent = `Visitas (esta sesion del navegador): ${nuevasVisitas}`;
    }

    const btn = document.getElementById("btn-cambiar-texto");
    const texto = document.getElementById("texto-dinamico");

    if (btn && texto) {
        btn.addEventListener("click", () => {
            texto.textContent = "¡El texto cambio con JavaScript!";
        });
    }
});
