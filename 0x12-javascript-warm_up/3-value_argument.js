#!/usr/bin/node

require('process');

if (2 in process.argv) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
