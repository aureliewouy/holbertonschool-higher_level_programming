#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const newlist = list.map((k, v) => k * v);
console.log(newlist);
