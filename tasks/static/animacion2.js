document.addEventListener("DOMContentLoaded", function() {
  const personasList = document.getElementById("personas-list");
  const personasItems = personasList.querySelectorAll(".persona-item");

  window.addEventListener("scroll", function() {
    personasItems.forEach(item => {
      if (item.offsetTop - window.innerHeight <= window.pageYOffset) {
        item.classList.add("visible");
      } else {
        item.classList.remove("visible");
      }
    });
  });
});
