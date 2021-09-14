#!/usr/bin/node

require('process');
const request = require('request');
const epi = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + epi;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  console.log(JSON.parse(body).title);
});
