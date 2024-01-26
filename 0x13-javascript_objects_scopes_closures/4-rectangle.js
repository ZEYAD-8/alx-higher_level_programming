#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (x) {
    let i = 0;
    while (i < this.height) {
      console.log(x.repeat(this.width));
      i++;
    }
  }

  rotate () {
    this.width += this.height;
    this.height = this.width - this.height;
    this.width -= this.height;
    // or just simply
    // [this.width, this.height] = [this.height, this.width]
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
