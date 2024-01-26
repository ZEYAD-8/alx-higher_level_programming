#!/usr/bin/node

exports.converter = function (base) {
  return function (decimalNumber) {
    return decimalNumber.toString(base);
  };
};
