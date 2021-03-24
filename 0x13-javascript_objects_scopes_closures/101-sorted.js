#!/usr/bin/node
const dict = require('./101-data').dict;
const newdict = {};
let k;

for (k in dict) {
  const v = dict[k];
  if (!newdict[v]) {
    newdict[v] = [k];
  } else {
    newdict[v].push(k);
  }
}
console.log(newdict);
