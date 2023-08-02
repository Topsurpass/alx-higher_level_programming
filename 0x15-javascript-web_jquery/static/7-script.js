$( ()=> {
  let url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.get(url, (data, status)=> {
	if (status == 'success') {
	    $('#character').text(data.name);
	}
  });
});

