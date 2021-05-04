#!/usr/bin/node
const url = process.argv.slice(2);
const request = require('request');
let nb = 0;
request(url[0], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const jsonBody = JSON.parse(body);
  const results = jsonBody.results;
  for (const element of results) {
    for (const c of element.characters) {
      if (c.includes("18")) {
        nb = nb + 1;
      }
    }
  }
  console.log(nb);
});
