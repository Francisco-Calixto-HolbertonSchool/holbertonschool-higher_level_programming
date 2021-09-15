#!/usr/bin/node

require('process');
const request = require('request');
const id = process.argv[2];
const ids_arr = [];
const url = 'https://swapi-api.hbtn.io/api/films/' + id

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  for (let i = 0; i < JSON.parse(body).characters.length; i++) {
    ids_arr.push(JSON.parse(body).characters[i].replace('https://swapi-api.hbtn.io/api/people/', ''));
  }
  console.log(ids_arr);
});
