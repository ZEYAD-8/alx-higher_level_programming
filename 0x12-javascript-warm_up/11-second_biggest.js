#!/usr/bin/node
const args = process.argv.slice(2).map(Number).sort((a, b) => b - a);

if (args.length < 2) {
  console.log(0);
} else {
  console.log(args[1]);
}
