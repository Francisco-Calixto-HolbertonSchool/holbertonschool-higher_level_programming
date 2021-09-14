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
        console.log(typeof(r));
        break
        if (!(task.userId in output) && task.completed) {
            output[task.userId.toString(10)] = 1;
        }
        else if (task.completed) {
            output[task.userId.toString(10)] += 1;
        }
    }
    console.log(output);
});
