#!/usr/bin/node
const url = process.argv.slice(2);
const request = require('request');
request.get(url[0], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  let usr = 1;
  const arr = {};
  let completed = 0;
  const jsonBody = JSON.parse(body);
  for (const element of jsonBody) {
    if (usr !== element.userId) {
      if (completed > 0) {
        arr[usr] = completed;
      }
      completed = 0;
      usr++;
    }
    if (element.completed === true) {
      completed++;
    }
  }
  if (completed > 0) {
    arr[usr] = completed;
  }
  console.log(arr);
});
