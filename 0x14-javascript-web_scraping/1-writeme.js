#!/usr/bin/node
const file = process.argv.slice(2);
const content = file[1];
const fs = require('fs');
fs.writeFile(file[0], content, err => {
  if (err) {
    console.error(err);
  }
});
