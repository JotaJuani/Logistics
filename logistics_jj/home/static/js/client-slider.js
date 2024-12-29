document.addEventListener("DOMContentLoaded", function () {
    const logos = document.querySelector(".logos");
    const clone = logos.cloneNode(true);
    logos.parentNode.appendChild(clone);
  });