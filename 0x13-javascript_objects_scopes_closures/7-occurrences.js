#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (const element of list) {
    if (element === searchElement) {
      counter++;
    }
  }
  return counter;
};
