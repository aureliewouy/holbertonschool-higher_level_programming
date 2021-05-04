#!/usr/bin/node
const url = process.argv.slice(2);
const request = require('request');
const wedge = '18';
let nb = 0;
request(url[0], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const jsonBody = JSON.parse(body);
  const results = jsonBody.results;
  for (const element of results) {
    for (const c of element.characters) {
      if (c === 'https://swapi-api.hbtn.io/api/people/' + wedge + '/') {
        nb = nb + 1;
      }
    }
  }
  console.log(nb);
});
