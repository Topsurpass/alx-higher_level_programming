 $('document').ready(()=> {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $('#btn_translate').on('click', ()=> {
    $.get(url + $.param({ lang: $('#language_code').val() }), (data)=> {
      $('#hello').text(data.hello);
    });
  });
});
