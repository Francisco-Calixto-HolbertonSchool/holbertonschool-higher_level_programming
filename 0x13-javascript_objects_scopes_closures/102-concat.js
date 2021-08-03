#!/usr/bin/node

const argv = require('process').argv;
const fs = require('fs');

fs.readFile('./' + argv[2], function (_err, data) {
  fs.readFile('./' + argv[3], function (_err2, data2) {
    const str = data + data2;
    fs.writeFile('./' + argv[4], str, function () {});
  });
});
