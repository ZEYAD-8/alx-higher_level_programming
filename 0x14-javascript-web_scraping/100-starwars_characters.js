#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(body);
  const charactersCount = data.characters.length;
  for (let z = 0; z < charactersCount; z++) {
    request(data.characters[z], (err, response, body) => {
      if (err) { return; }
      const charData = JSON.parse(body);
      console.log(charData.name);
    });
  }
});
