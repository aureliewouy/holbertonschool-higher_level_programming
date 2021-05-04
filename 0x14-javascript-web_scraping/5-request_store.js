#!/usr/bin/node
const args = process.argv.slice(2);
const url = args[0];
const file = args[1];
const request = require('request');
const fs = require('fs');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file, body, err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
