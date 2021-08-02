#!/usr/bin/node

require('process');

const x = process.argv[2];

if (x === undefined || isNaN(parseInt(x))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
