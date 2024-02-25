#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/people/18/';
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(body);
  console.log(data.films.length);
});
