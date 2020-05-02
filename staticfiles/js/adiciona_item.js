
let quantidade = $("#qtd");
let valor = $("#preco").text();
let disponivel = $("#disponivel").text();

$("#mensagem").hide();

quantidade.on("click", () =>{
  preco = valor.replace("R$ ", "");
  preco = preco.replace(",", ".");
  preco = parseFloat(preco);

  item = quantidade.val();
  console.log(item);
  
  item = parseInt(item);
  total = preco * item;
  total = total.toFixed(2);
  $('#total').text(`R$ ${total}`);

  let qtdetotal = parseInt(disponivel);
 if (item >= qtdetotal){
   $("#qtd").prop("disabled", true);
  $("#mensagem").show();
 }
})


let qtde_solicitada = $("#qtde_solicitada").text();
  console.log(qtde_solicitada);

let total = $("#total").text();
console.log(total);
