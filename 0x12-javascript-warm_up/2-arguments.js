#!/usr/bin/node

const argnum = process.argv.length;
if (argnum === 3) {
  console.log('Argument found');
} else if (argnum > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
