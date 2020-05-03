
$('#botao').click("submit" ,function(event) {
  event.preventDefault();
  
  $.ajax({
    url: "/produtos/add_carrinho/",
    type: "post", // or "get"
    data: {
      quantidade: quantidade = $("#qtd").val(),
      total: total = $("#total").val() ,
      csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
      action: 'post'
    },
    success: function(data) {
  
        alert(total);
    },
    error: function(xhr, status, e) {
      alert(status, e);
  }});

 
});
