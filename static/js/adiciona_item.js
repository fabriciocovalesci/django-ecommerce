
let quantidade = $("#qtd");
let valor = $("#preco").text();
let disponivel = $("#disponivel").text();
let icone = $("#icone")

$("#mensagem").hide();

quantidade.on("click", () =>{
  preco = valor.replace("R$ ", "");
  preco = preco.replace(",", ".");
  preco = parseFloat(preco);

  item = quantidade.val();

  
  item = parseInt(item);
  total = preco * item;
  total = total.toFixed(2);
  $('#total').text(`R$ ${total}`);
  icone.text(` R$ ${total}`);
  console.log(icone)
  let qtdetotal = parseInt(disponivel);
 if (item >= qtdetotal){
   $("#qtd").prop("disabled", true);
  $("#mensagem").show();
 }
})


