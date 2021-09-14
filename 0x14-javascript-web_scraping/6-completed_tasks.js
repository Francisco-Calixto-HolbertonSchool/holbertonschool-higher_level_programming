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
    for (task in r) {
        if (!(task.userId in output) && task.completed) {
            output[task.userId] = 1;
            continue;
        }
        if (task.completed) {
            output[task.userId] += 1;
            continue;
        }
    }
    console.log(output);
});
