#!/usr/bin/node

require('process');

const list = process.argv;
if (list.length < 4) {
  console.log(0);
} else {
  const aux = [];
  for (let i = 2; list[i] !== undefined; i++) {
    aux.push(parseInt(list[i]));
  }
  aux.sort();
  aux.pop();
  console.log(aux[aux.length - 1]);
}
