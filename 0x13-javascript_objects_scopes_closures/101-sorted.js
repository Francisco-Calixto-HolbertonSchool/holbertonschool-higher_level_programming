#!/usr/bin/node

const dict = require('./101-data').dict;
const cpy = {};

for (const [key, value] of Object.entries(dict)) {
  if (cpy[String(value)] === undefined) {
    cpy[String(value)] = [key];
  } else {
    cpy[String(value)].push(key);
  }
}
console.log(cpy);
