$(() => {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, (data, status) => {
    if (status === 'success') {
      const resArr = data.results;
      for (const i in resArr) {
        const item1 = $('<li></li>').text(resArr[i].title);
        $('#list_movies').append(item1);
      }
    }
  });
});
