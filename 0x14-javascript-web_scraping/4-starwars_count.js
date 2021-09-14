#!/usr/bin/node

require('process');
const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const results = JSON.parse(body).results
  for (let i = 0; i < results.length ; i++) {
    console.log(results[i]);
    for (let j = 0; j < results[i].length ; j++) {
        console.log(results[i][j]);
        if (results[i][j] == 'https://swapi-api.hbtn.io/api/people/18/') {
            count++;
        }
    }
  }
  console.log(count);
});
