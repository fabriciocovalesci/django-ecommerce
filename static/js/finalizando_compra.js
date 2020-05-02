

let quantidade_solitado = $("#qtd");
let valorProduto = $("#preco").text();


quantidade_solitado.on("click", () =>{
  preco = valorProduto.replace("R$ ", "");
  preco = preco.replace(",", ".");
  preco = parseFloat(preco);

  item = quantidade.val();

  item = parseInt(item);
  total = preco * item;
  total = total.toFixed(2);
  $('#total').text(`R$ ${total}`);

 console.log(total)


})

$("#qtd").change(function () {
    var qtde = $(this).text();

    $.ajax({
      url: '/produtos/comprando/',
      data: {
        'qtde': qtde
      },
      dataType: 'json',
      success: function (data) {
        if (data.is_taken) {
          alert("funcionou");
          console.log("ajax");
        }
      }
    });

  });

// $.ajax({
//     url:  '/produtos/comprando',
//     type:  'get',
//     dataType:  'json',
//     success: function  (data) {
//         let rows =  '';
//         data.rooms.forEach(room => {
//         rows += `
//         <tr>
//             <td>${room.room_number}</td>
//             <td>${room.name}</td>
//             <td>${room.nobeds}</td>
//             <td>${room.room_type}</td>
//             <td>
//                 <button class="btn deleteBtn" data-id="${room.id}">Delete</button>
//                 <button class="btn updateBtn" data-id="${room.id}">Update</button>
//             </td>
//         </tr>`;
//     });
//     $('[#myTable](https://paper.dropbox.com/?q=%23myTable) > tbody').append(rows);
//     $('.deleteBtn').each((i, elm) => {
//         $(elm).on("click",  (e) => {
//             deleteRoom($(elm))
//         })
//     })
//     }
// });



//     let nome_produto = $("#nome_produto").text();

//     let qtde_solicitada = $("#qtd").text()

// let total_pagar = $("#total").text()

// let finaliza_nome = $("#nome").text(nome_produto);
// console.log(finaliza_nome);

// let finaliza_qtd = $("#quantidade").text(qtde_solicitada);
// console.log(finaliza_qtd);

// let finaliza_total_pagar = $("#total_pagar").text(total_pagar);
// console.log(finaliza_total_pagar);

// let nome = $("#meunome").text();
// console.log(nome);
    



