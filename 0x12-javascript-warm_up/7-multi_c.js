#!/usr/bin/node

let converted = parseInt(process.argv[2]);
if (!converted) {
  console.log('Missing number of occurrences');
} else {
  while (converted > 0) {
    console.log('C is fun');
    converted--;
  }
}
