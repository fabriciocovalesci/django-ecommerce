
$('#botao').click("submit" ,function(event) {
  event.preventDefault();
  let quantidade = $("#qtd").val();
  let total = $("#total").val();

  $.ajax({
      type: 'POST',
      url: '/produtos/add_carrinho/',
      data: {
        quantidade: "quantidade",
        total: "total",
        csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
    },
      success: function () {
        console.log(total)
        console.log(quantidade)
      },
      error: function(xhr, status, e) {
          alert(status, e);
      }
  });
});
