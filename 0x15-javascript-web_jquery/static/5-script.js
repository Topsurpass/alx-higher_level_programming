$( ()=> {
  $('#add_item').on('click', ()=> {
     let item1 = $("<li></li>").text("Item");
     $('ul.my_list').append(item1);
  })
});

