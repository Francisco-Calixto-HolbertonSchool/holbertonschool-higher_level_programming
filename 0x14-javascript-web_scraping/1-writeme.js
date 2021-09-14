#!/usr/bin/node

require('process');
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], {
  encoding: 'utf8',
  flag: 'w',
  mode: 0o666
}, (err) => {
  if (err) {
    console.error(err);
  }
});
