#!/usr/bin/node
const id = process.argv.slice(2);
const url = 'https://swapi-api.hbtn.io/api/films/' + id[0];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const jsonBody = JSON.parse(body);
  for (const c of jsonBody.characters) {
    request(c, function (error, response, body) {
      if (error) {
        console.error(error);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
