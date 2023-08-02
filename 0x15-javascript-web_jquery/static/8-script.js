$( ()=> {
  let url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, (data, status)=> {
	if (status == 'success') {
	    let resArr = data.results;
	    for (let i in resArr)
	    {
     		let item1 = $("<li></li>").text(resArr[i].title);
	    	$('#list_movies').append(item1);
	    }
	}
  });
});

