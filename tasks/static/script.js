const skillsButton = document.getElementById('skills-button');
const skillsList = document.getElementById('skills-list');

skillsButton.addEventListener('click', () => {
  if (skillsList.style.display === 'none') {
    skillsList.style.display = 'block';
  } else {
    skillsList.style.display = 'none';
  }
});


  // Aplicar la transformación a imagen
var image = document.getElementById("profile-picture");
var jump = 0;
var jumpIn = true;

setInterval(function() {

  if (jumpIn) {
    jump += 50;
  } else {
    jump -= 50;
  }

  if (jump >= 20) {
    jumpIn = false;
  } else if (jump <= 0) {
    jumpIn = true;
  }
  
  image.style.transform = "translateY(-" + jump + "px) scale(" + (1 + (jump / 200)) + ")";
}, 1000);



  const input = document.getElementById("busqueda");
  const resultados = document.getElementById("tabla-productos");

  input.addEventListener("keyup", function(event) {
    const busqueda = event.target.value.toLowerCase();
    const filas = resultados.getElementsByTagName("tr");

    for (let i = 0; i < filas.length; i++) {
      const celdas = filas[i].getElementsByTagName("td");
      let mostrar = false;

      for (let j = 0; j < celdas.length; j++) {
        const texto = celdas[j].textContent.toLowerCase();
        if (texto.indexOf(busqueda) !== -1) {
          mostrar = true;
          break;
        }
      }

      if (mostrar) {
        filas[i].style.display = "";
      } else {
        filas[i].style.display = "none";
      }
    }
  });



