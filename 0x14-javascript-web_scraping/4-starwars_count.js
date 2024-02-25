#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(body);

  let count = 0;
  for (let i = 0, len = data.results.length; i < len; i++) {
    for (let z = 0, len = data.results[i].characters.length; z < len; z++) {
      const Test = data.results[i].characters[z];
      if (Test.includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
