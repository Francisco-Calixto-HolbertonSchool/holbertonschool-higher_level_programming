#!/usr/bin/node

const list = require('./100-data').list;

const aux = list.map((n, index) => n * index);
console.log(list);
console.log(aux);
