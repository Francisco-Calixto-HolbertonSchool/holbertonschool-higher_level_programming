#!/usr/bin/node

require('process');
const request = require('request');
const url = process.argv[2];
const count = 0;
const results;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  results = JSON.parse(body).results
  for (let i = 0; i < results.length ; i++) {
    for (let j = 0; j < results[i].length ; j++) {
        if (results[i][j] == 'https://swapi-api.hbtn.io/api/people/18/') {
            count++;
        }
    }
  }
  console.log(count);
});
