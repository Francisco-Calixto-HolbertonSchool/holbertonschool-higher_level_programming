#!/usr/bin/node

exports.esrever = function (list) {
  const l = list.length - 1;
  const arrcpy = [];
  for (let i = l; i >= 0; i--) {
    arrcpy.push(list[i]);
  }
  return arrcpy;
};
