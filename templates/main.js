var button = document.getElementById("action");

button.addEventListener("click", function(){
  var cont = document.getElementById("cont");
  cont.classList.toggle("hide");
});

var button = document.getElementById("action1");

button.addEventListener("click", function(){
  var endereco = document.getElementById("endereco");
  endereco.classList.toggle("hide");
});

var button = document.getElementById("action-formacao");

button.addEventListener("click", function(){
  var grau = document.getElementById("grau-formacao");
  grau.classList.toggle("hide");
});

var button = document.getElementById("action-contato");

button.addEventListener("click", function(){
  var contato = document.getElementById("user-contato");
  contato.classList.toggle("hide");
});


