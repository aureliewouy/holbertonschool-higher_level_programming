#!/usr/bin/node
const id = process.argv.slice(2);
const url = 'https://swapi-api.hbtn.io/api/films/' + id[0];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const jsonBody = JSON.parse(body);
  let i = [];
  for (i = 0; i < jsonBody.characters.length; i++) {
    request(jsonBody.characters[i], function (error, response, body) {
      if (error) {
        console.error(error);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
