#!/usr/bin/node
const Rectangle = class {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return Rectangle === {};
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const inter = this.width;
    this.width = this.height;
    this.height = inter;
  }

  double () {
    (this.height = this.height * 2);
    (this.width = this.width * 2);
  }
};
module.exports = Rectangle;
