$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
  const results = data.results;
  for (let i = 0; i < results.length; i++) {
    $('#list_movies').append('<li>' + results[i].title + '</li>');
  }
});
