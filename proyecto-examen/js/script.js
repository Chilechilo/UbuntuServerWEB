window.addEventListener("DOMContentLoaded", () => {
  alert("Welcome! [HyperLink Blocked], time to be a [Big Shot]!");

  const colores = ["#f4f7fb", "#ffe9a8", "#c8f7c5", "#d7e7ff", "#ffd7e0", "#e7d7ff"];
  let i = 0;

  const btn = document.getElementById("btn-fondo");
  if (btn) {
    btn.addEventListener("click", () => {
      i = (i + 1) % colores.length;
      document.body.style.backgroundColor = colores[i];
    });
  }
});


