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
    console.log(typeof(r));
    console.log(typeof(r[0]));
    console.log(r[0]);
    for (task in JSON.parse(body)) {
        break;
        if (!(task.userId in output) && task.completed) {
            output[task.userId.toString(10)] = 1;
        }
        else if (task.completed) {
            output[task.userId.toString(10)] += 1;
        }
    }
    console.log(output);
});
