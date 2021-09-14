#!/usr/bin/node

require('process');
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];
const fs = require('fs');

request (url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const content = JSON.parse(body);
  fs.writeFile(file, content, {
    encoding: 'utf8',
    flag: 'w',
    mode: 0o666
  }, (err) => {
    if (err) {
      console.error(err);
      return;
    }
  });
});
