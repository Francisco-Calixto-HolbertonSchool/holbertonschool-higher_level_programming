#!/usr/bin/node

require('process');
const request = require('request');
const id = process.argv[2];
const ids = [];
let url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  for (let i = 0; i < JSON.parse(body).characters.length; i++) {
    ids.push(JSON.parse(body).characters[i].replace('https://swapi-api.hbtn.io/api/people/', ''));
  }
  for (let j = 0; j < ids.length; j++) {
    url = 'https://swapi-api.hbtn.io/api/people/' + ids[j];
    request(url, function (error, response, body) {
      if (error) {
        console.log(error);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  }
});
