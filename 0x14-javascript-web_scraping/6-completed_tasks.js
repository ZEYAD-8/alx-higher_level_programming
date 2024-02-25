#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(body);
  const TasksCount = data.length;
  const dic = {};
  for (let z = 0; z < TasksCount; z++) {
    if (data[z].completed === false) { continue; }
    if (data[z].userId in dic) { dic[data[z].userId]++; } else { dic[data[z].userId] = 1; }
  }
  console.log(dic);
});
