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
    for (task in body) {
        const t = JSON.parse(task);
        console.log(typeof(t));
        console.log(t);
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
