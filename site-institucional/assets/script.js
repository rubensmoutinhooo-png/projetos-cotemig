// script do site
// abre/fecha o menu no celular e valida o formulario de contato

document.addEventListener("DOMContentLoaded", function () {
  var botaoMenu = document.querySelector(".menu-toggle");
  var linksMenu = document.querySelector(".nav-links");

  if (botaoMenu) {
    botaoMenu.addEventListener("click", function () {
      linksMenu.classList.toggle("aberto");
    });
  }

  var formulario = document.querySelector("#form-contato");
  if (formulario) {
    formulario.addEventListener("submit", function (evento) {
      evento.preventDefault();

      var nome = document.querySelector("#nome").value;
      var email = document.querySelector("#email").value;
      var mensagem = document.querySelector("#mensagem").value;
      var status = document.querySelector("#status-formulario");

      if (nome == "" || email == "" || mensagem == "") {
        status.innerHTML = "preenche todos os campos";
        status.className = "mensagem-status erro";
        return;
      }

      if (email.indexOf("@") == -1) {
        status.innerHTML = "email invalido";
        status.className = "mensagem-status erro";
        return;
      }

      status.innerHTML = "Mensagem enviada com sucesso!";
      status.className = "mensagem-status sucesso";
      formulario.reset();
    });
  }
});
