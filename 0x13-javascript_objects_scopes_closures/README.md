# 0x13. Javascript - Objects, Scopes and Closures

## General Requirements
- Allowed editors: **vi**, **vim**, **emacs**
- All files were interpreted on Ubuntu 20.04 LTS using ``node`` (version 14.x)
- All files ends with a new line
- The first line of all the files has exactly ``#!/usr/bin/node``
- My code is ``semistandard`` compliant (version 16.x.x). [Rules of Standard](https://standardjs.com/rules.html) + [semicolons on top](https://github.com/standard/semistandard). Also as reference: [AirBnB style](https://github.com/airbnb/javascript)
- All files are executable

## More Info
**Install Node 14**
``
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
``
**Install semi-standard**
[Documentation](https://github.com/standard/semistandard#JavaScript Semi-Standard Style)
``$ sudo npm install semistandard --global``

### Resources
**Read or watch:**
- [JavaScript object basics](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics)
- [Object-oriented JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)
- [Class - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
- [super - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
- [extends - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
- [Object prototypes](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes)
- [Inheritance in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)
- [Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
- [this/self](https://alistapart.com/article/getoutbindingsituations/)
- [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)
- [Array.prototype.map()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map?v=control)

## Table of contents
Files | Description
----- | -----------
[0-rectangle.js](./0-rectangle.js) | empty class Rectangle that defines a rectangle
[1-rectangle.js](./1-rectangle.js) | class Rectangle that defines a rectangle
[2-rectangle.js](./2-rectangle.js) | class Rectangle that defines a rectangle
[3-rectangle.js](./3-rectangle.js) | class Rectangle that defines a rectangle
[4-rectangle.js](./4-rectangle.js) | class Rectangle that defines a rectangle
[5-square.js](./5-square.js) | class Square that defines a square and inherits from Rectangle of 4-rectangle.js
[6-square.js](./6-square.js) | class Square that defines a square and inherits from Square of 5-square.js
[7-occurrences.js](./7-occurrences.js) | JS function that returns the number of occurrences in a list
[8-esrever.js](./8-esrever.js) | JS function that returns the reversed version of a list
[9-logme.js](./9-logme.js) | JS function that prints the number of arguments already printed and the new argument value
[10-converter.js](./10-converter.js) | JS function that converts a number from base 10 to another base passed as argument