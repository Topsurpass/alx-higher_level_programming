$('document').ready(() => {
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.get(url, (data) => {
    $('div#hello').text(data.hello);
  });
});
