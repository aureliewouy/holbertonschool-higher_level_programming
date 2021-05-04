#!/usr/bin/node
const url = process.argv.slice(2);
const request = require('request');
request(url[0], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log('Code:', response && response.statusCode);
});
