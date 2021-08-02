#!/usr/bin/node

require('process');

function add (a, b) {
  const c = parseInt(a);
  const d = parseInt(b);
  if (isNaN(c) || isNaN(d)) {
    console.log(NaN);
  } else {
    console.log(c + d);
  }
}

add(process.argv[2], process.argv[3]);
