
$('#botao').click("submit" ,function(event) {
  event.preventDefault();
  
  $.ajax({
    url: "/produtos/add_carrinho/",
    type: "post", // ou "get"
    data: {
      quantidade: quantidade = $("#qtd").val(),
      total: total = $("#total").val() ,
      csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
      action: 'post'
    },
    success: function(data) {
      alert(`Dados adicionados ao carrinho de compra
            Quantidade total: ${quantidade} unidade(s)
            Valor final: ${total}`)
    },
    error: function(xhr, status, e) {
      alert(status, e);
  }});

 
});
