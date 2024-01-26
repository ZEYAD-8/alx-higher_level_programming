#!/usr/bin/node

const converted = parseInt(process.argv[2]);
if (converted) {
  console.log(converted);
} else {
  console.log('Not a number');
}
