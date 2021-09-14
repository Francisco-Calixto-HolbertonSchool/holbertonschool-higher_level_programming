#!/usr/bin/node

require('process');
const request = require('request');
const url = process.argv[2];
const output = {};

request(url, function (error, response, body) {
    if (error) {
      console.log(error);
      return;
    }
    const r = JSON.parse(body);
    for (let i = 0; i < r.length; i++) {
        if (!(r[i].userId in output) && r[i].completed) {
            output[r[i].userId.toString(10)] = 1;
        }
        else if (r[i].completed) {
            output[r[i].userId.toString(10)] += 1;
        }
    }
    console.log(output);
});
