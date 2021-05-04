#!/usr/bin/node
const file = process.argv.slice(2);
const fs = require('fs');
fs.readFile(file[0], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
